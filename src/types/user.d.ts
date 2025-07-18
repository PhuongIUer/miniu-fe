export interface Role {
  id: number;
  name: string;
}

export interface User {
  id: number;
  email: string;
  userName: string;
  avatar: string | null;
  major: string | null;
  position: string | null;
  office: string | null;
  role: Role;
}

export interface updateUser {
  avatar: File | string | null;
  userName: string; 
  major: string | null;
  position: string | null;
  office: string | null;
}

export interface newUser {
  email: string
  password: string
  userName: string
}

export interface access_token {
  access_token: string
}
