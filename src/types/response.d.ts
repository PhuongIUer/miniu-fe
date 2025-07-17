import type { User } from './user'

export interface UserResponse {
  items: User[];
  meta: {
    totalItems: number;
    itemsPerPage: number;
    totalPages: number;
    currentPage: number;
  };
}

export interface MajorResponse {
  id: number
  name: string
}

export interface CurriculumResponse {
  id: number
  name: string
  majors: any[]
}

export interface ConcentrationResponse {
  id: number
  name: string
}

export interface SemesterResponse {
  id: number
  name: string
}

export interface SubjectResponse {
  name: string
  credits: number
}