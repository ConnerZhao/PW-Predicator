import pandas as pd
import random
from joblib import load
import tkinter as tk
from tkinter import messagebox
import warnings
warnings.filterwarnings("ignore", category=UserWarning, 
        message="X has feature names, but")
# loading pre-traied model
model = load('trained model/model.joblib')



# Define your feature names here, as per the trained model's requirements
feature_names = ['length', 'uppercase_letters', 'lowercase_letters', 'digits', 'special_characters', 'numerical_characters', 'alphabetical_characters']

# Function to extract features from a password
def extract_features(password):
    features = {
        'length': len(password),
        'uppercase_letters': sum(1 for c in password if c.isupper()),
        'lowercase_letters': sum(1 for c in password if c.islower()),
        'digits': sum(1 for c in password if c.isdigit()),
        'special_characters': sum(1 for c in password if not c.isalnum()),
        'numerical_characters': 1 if any(c.isdigit() for c in password) else 0,
        'alphabetical_characters': 1 if any(c.isalpha() for c in password) else 0
    }
    return features

# Function to suggest improvements and generate an example of a good password
def suggest_and_generate_improvements(password):
    features = extract_features(password)
    suggestions = []
    improved_password = list(password)

    if features['length'] < 8:
        suggestions.append("Make the password at least 8 characters long.")
        # Add random characters to make password at least 8 characters long
        while len(improved_password) < 8:
            improved_password.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!'))

    if features['uppercase_letters'] == 0:
        suggestions.append("Add at least one uppercase letter.")
        # Convert a random character to uppercase
        improved_password[random.randint(0, len(improved_password)-1)] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if features['lowercase_letters'] == 0:
        suggestions.append("Add at least one lowercase letter.")
        # Convert a random character to lowercase
        improved_password[random.randint(0, len(improved_password)-1)] = random.choice('abcdefghijklmnopqrstuvwxyz')

    if features['digits'] == 0:
        suggestions.append("Include at least one digit.")
        # Insert a digit at a random position
        improved_password.insert(random.randint(0, len(improved_password)-1), random.choice('0123456789'))

    if features['special_characters'] == 0:
        suggestions.append("Include at least one special character (e.g., @, #, $).")
        # Insert a special character at a random position
        improved_password.insert(random.randint(0, len(improved_password)-1), random.choice('@#$!'))

    if features['numerical_characters'] == 0:
        suggestions.append("Make sure the password has numbers in it.")
        # Insert a digit at a random position
        improved_password.insert(random.randint(0, len(improved_password)-1), random.choice('0123456789'))

    if features['alphabetical_characters'] == 0:
        suggestions.append("Make sure the password has letters in it.")
        # Insert a letter at a random position
        improved_password.insert(random.randint(0, len(improved_password)-1), random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Shuffle the improved password to avoid predictability
    random.shuffle(improved_password)
    improved_password = ''.join(improved_password)

    return suggestions, improved_password

# GUI application
class PasswordApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Strength Predictor")
        self.password_visible = False  # Flag to toggle password visibility
        self.create_widgets()

    def create_widgets(self):
        # Password entry
        self.password_label = tk.Label(self, text="Enter your password:")
        self.password_label.pack()
        
        self.password_entry_frame = tk.Frame(self)
        self.password_entry = tk.Entry(self.password_entry_frame, show="*", width=47)
        self.password_entry.pack(side="left", padx=(0, 2))

        # Toggle password visibility button
        self.toggle_password_button = tk.Button(self.password_entry_frame, text="Show", command=self.toggle_password)
        self.toggle_password_button.pack(side="right")
        self.password_entry_frame.pack()

        # Predict button
        self.predict_button = tk.Button(self, text="Check Password Strength", command=self.predict_password_strength)
        self.predict_button.pack()

        # Result display
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        # Suggestions display
        self.suggestions_label = tk.Label(self, text="")
        self.suggestions_label.pack()

        # Improved password display
        self.improved_password_label = tk.Label(self, text="")
        self.improved_password_label.pack()

    def toggle_password(self):
        if self.password_visible:
            self.password_entry.config(show="*")
            self.toggle_password_button.config(text="Show")
        else:
            self.password_entry.config(show="")
            self.toggle_password_button.config(text="Hide")
        self.password_visible = not self.password_visible

    def predict_password_strength(self):
        # Get password
        user_password = self.password_entry.get()
        # Check if password is not empty
        if not user_password:
            messagebox.showerror("Error", "Please enter a password.")
            return

        # Predict strength
        features = extract_features(user_password)
        features_df = pd.DataFrame([features], columns=feature_names)
        predicted_strength = model.predict(features_df)[0]

        # Determine strength label
        strength_label = {0: 'Weak', 1: 'Medium', 2: 'Strong'}
        predicted_strength_label = strength_label[predicted_strength]

        # Display result
        self.result_label.config(text=f"Predicted strength: {predicted_strength_label}")

        # Provide suggestions and improved password if not strong
        if predicted_strength_label != 'Strong':
            suggestions, improved_password = suggest_and_generate_improvements(user_password)
            suggestions_text = "Suggestions to improve your password:\n" + "\n".join(suggestions)
            self.suggestions_label.config(text=suggestions_text)
            self.improved_password_label.config(text=f"Example of a stronger password: {improved_password}")
        else:
            self.suggestions_label.config(text="")
            self.improved_password_label.config(text="")

# Run the application
if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()