export interface MajorLecturerList {
  majorLecturers: MajorLecturer[]
}

export interface MajorLecturer {
  majorName: string
  lecturers: Lecturer[]
}

export interface Lecturer {
  name: string
  position: string
  email: string
  office: string
  imageUrl: string
}


export interface RegisterResponse {
  id: number
  email: string
  role: string
  message: string
}

export interface responseLecturer {
  id: number
  email: string
  userName: string
  avatar: string
  major: string
  position: string
  office: string
  role: Role
}

export interface Role {
  id: number
  name: string
}
