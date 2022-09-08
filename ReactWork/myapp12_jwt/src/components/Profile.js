import { Modal } from "react-bootstrap";
import AuthService from "../services/auth-service"


const Profile = () => {
    const currentUser = AuthService.getCurrentUser();
    return (
        <Modal.Dialog>
            <Modal.Header closeButton>
                <Modal.Title><strong>Profile</strong></Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <p><strong>Token :</strong>{currentUser.accessToken.substring(0, 20)}...{" "}
                    {currentUser.accessToken.substr(currentUser.accessToken.length - 20)} </p>
                <p><strong>Id : </strong>{currentUser.id}</p>
                <p><strong>Email : </strong>{currentUser.email}</p>
                <p><strong>Role : </strong>{currentUser.role}</p>
            </Modal.Body>

        </Modal.Dialog>
    )
}

export default Profile;