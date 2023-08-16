uninstall plugin validate_password;
ALTER USER 'root'@'localhost' IDENTIFIED BY '';
UNINSTALL COMPONENT "file://component_validate_password";
