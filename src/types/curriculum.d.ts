export interface Curriculum {
  name: string
  majors: Major[]
}

export interface Major {
  name: string
  concentrations: Concentration[]
}

export interface Concentration {
  name: string 
  semesters: Semester[]
}

export interface Semester {
  name: string
  subjects: Subject[]
}

export interface Subject {
  name: string
  credits: number
}
