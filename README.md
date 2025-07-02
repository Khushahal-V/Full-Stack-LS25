# Full-Stack-LS25
week 3 assignment


# YouTube Clone – Django Backend (Week 3)

This Django project implements the backend for a YouTube-like application with user authentication, simulated email verification, and a protected dashboard.

---

## Features Implemented

### 1. User Registration
- Fields: Username, Email, Password, Confirm Password
- Validations:
  - Email must be unique
  - Passwords must match
- Used Django’s `UserCreationForm` wrapped in a custom `ModelForm`

### 2. Simulated Email Verification
- After registration, user is redirected to `/verify/<token>/`
- No actual email sent (simulation only)
- Sets user account to active on verification
- Displays success message: "Account Verified Successfully"

### 3. Login and Logout
- Login form authenticates credentials
- Displays errors for incorrect credentials or inactive accounts
- Logout button provided on the dashboard

### 4. Protected Dashboard
- Accessible only after login
- Shows user-specific information: email, verification status, join date
- Uses Django’s `@login_required` decorator

### 5. Django Admin Panel
- Superuser can access `/admin/`
- `Profile` model is registered in the admin panel with:
  - `list_display`
  - `search_fields`
  - `ordering`
- Organized layout for user management

### 6. Styled Templates
- HTML pages styled using Bootstrap
- Templates include:
  - `register.html`
  - `login.html`
  - `dashboard.html`
  - `verify.html`
- Basic navbar with login/logout links
