# BashaKhuji - House Rental Website

## Overview
BashaKhuji is a web-based platform designed to help users find and list rental properties with ease. The platform enables property owners to post available properties, while tenants can search and filter rental options based on their preferences. The website is built using Django for the backend, SQLite3 for the database, and Tailwind CSS for the frontend.

## Features
 
- **User Authentication**: Users can sign up, log in, and manage their profiles.
  ![Image](https://github.com/user-attachments/assets/2b396cfa-5215-457a-a869-0c92bcb5a627)
- **Property Listings**: Users can add, edit, and delete property listings.
  ![Image](https://github.com/user-attachments/assets/4e812eb4-313b-413d-880e-db0e62712bfc)
- **Search and Filter**: Search properties based on location, price, bedrooms, and more.
  ![Image](https://github.com/user-attachments/assets/7764948b-d14e-4ac7-9f4c-b39f173b9d8f)
- **Detailed Property View**: Each property has a dedicated page with details and images.
  ![Image](https://github.com/user-attachments/assets/2d4c49f4-289d-4e6a-8b49-9ccca9e3d693)
- **Responsive Design**: Optimized for all devices with a modern UI using Tailwind CSS.
- **Secure and Scalable**: Uses Django's built-in security features.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- Git
- Virtual environment (`venv` or `virtualenv`)

### Steps to Set Up Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/mirrahman109/BashaKhuji.git
   cd BashaKhuji
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to enter username, email, and password.

6. Run the development server:
   ```sh
   python manage.py runserver
   ```
   The website will be available at `http://127.0.0.1:8000/`

## Usage
- **Users**: Sign up, log in, and browse rental properties.
- **Property Owners**: Add, manage, and delete listings.
- **Admin Panel**: Accessible at `/admin` for managing users and properties.

## Contributing
If you'd like to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For any queries or support, feel free to reach out to:
- **Developer**: Mir Rahman
- **Email**: mirrahman109@gmail.com
- **GitHub**: [mirrahman109](https://github.com/mirrahman109)

---
Feel free to modify this README as per your project requirements!

