# OkCanteen 🍽️

## Introduction
**OkCanteen** is a modern and efficient **Canteen Management System** designed to streamline the ordering process for students and staff. It enables users to place orders online, reducing queues and improving service efficiency. With secure authentication, categorized menus, and real-time order tracking, OkCanteen enhances the overall canteen experience.

## Features 🚀
- **Online Ordering**: Students and staff can place orders from anywhere.
- **Secure Authentication**: Uses **JWT-based authentication** for login and access control.
- **Menu Management**: Canteen admins can add, update, or remove food items.
- **Order Tracking**: Users can track their order status in real time.
- **Student ID Verification**: Ensures only authorized users can access the system.
- **FastAPI Backend**: Provides a high-performance and scalable backend.
- **Database Support**: Uses PostgreSQL/MongoDB for efficient data management.

## Tech Stack 🛠️
- **Backend**: FastAPI (Python)
- **Frontend**: React.js / Next.js (Optional for UI development)
- **Database**: PostgreSQL / MongoDB
- **Authentication**: JWT (JSON Web Token)
- **Deployment**: Docker, Cloud Hosting (AWS, GCP, or DigitalOcean)

## Installation 🏗️
### Prerequisites
- Python 3.9+
- PostgreSQL or MongoDB
- Node.js (if using a frontend)
- Docker (optional)

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/OkCanteen.git
   cd OkCanteen
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   cd Backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   fastapi dev src/main.py --port 5000
   ```
4. Access the API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Frontend Setup (Optional)
1. Navigate to the frontend directory:
   ```sh
   cd Frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm start
   ```

## API Endpoints 📡
| Method | Endpoint          | Description              |
|--------|------------------|--------------------------|
| POST   | `/auth/signup`   | Register a new user     |
| POST   | `/auth/login`    | Authenticate user       |
| GET    | `/menu`          | Fetch available items   |
| POST   | `/order`         | Place a new order       |
| GET    | `/order/{id}`    | Get order details       |

## Future Enhancements 🌟
- Mobile App Integration 📱
- AI-based Order Recommendation 🤖
- Payment Gateway Integration 💳
- Analytics Dashboard 📊

## Contributing 🤝
We welcome contributions! Feel free to **fork** the repo, create a new branch, and submit a **pull request**.

## License 📜
This project is licensed under the **MIT License**.

---
**Developed with ❤️ for Smart Canteens!**
