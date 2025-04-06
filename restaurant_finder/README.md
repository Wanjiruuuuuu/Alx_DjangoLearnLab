# 🍽️ Restaurant Finder App

The **Restaurant Finder App** helps users easily discover restaurants based on location, budget, and preferences such as outdoor seating, live music, and more. Users can view restaurant profiles, including images, menus, customer reviews, and a map of the location.

---

## 🔧 Features

- 🔍 **Search & Filter Restaurants** by:
  - Location
  - Budget
  - Alphabetical order
  - Tags (e.g., family-friendly, live music, vegan, etc.)

- 🗺️ **Map Integration** to view restaurant location on the profile page

- 📸 **Restaurant Profiles** displaying:
  - Menu images
  - Reviews
  - Tags and features

- ❤️ **User-friendly interface** for easy navigation and selection

---

## 🛠️ Tech Stack

- **Frontend**: Flutter
- **Backend**: Firebase (authentication + Firestore database)
- **Image Storage**: Firebase Storage
- **APIs**: (Optional) Free third-party APIs for restaurant data *(under research)*

---

## 📁 Project Structure

```plaintext
lib/
├── main.dart
├── screens/
│   ├── home_screen.dart
│   ├── restaurant_profile.dart
├── widgets/
│   ├── search_bar.dart
│   ├── filter_tags.dart
├── models/
│   ├── restaurant_model.dart
├── services/
│   ├── firebase_service.dart
