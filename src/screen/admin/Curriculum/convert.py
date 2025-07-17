import json

def convert_structure(input_data):
    output = {"majors": []}
    
    # Duyệt qua các trường học (schools)
    for school_name, programs in input_data.items():
        major = {
                "name": school_name,
                "concentrations": []
            }
        for program_name, semesters in programs.items():
            
            # Tạo một concentration cho mỗi program
            concentration = {
                "name": program_name,
                "semesters": []
            }
            
            # Duyệt qua các học kỳ (semesters)
            for semester_name, subjects in semesters.items():
                semester = {
                    "name": semester_name,
                    "subjects": subjects
                }
                concentration["semesters"].append(semester)
            
            major["concentrations"].append(concentration)
            output["majors"].append(major)
    
    return output

# Dữ liệu đầu vào
input_data = {
  "School of Computer Science and Engineering": {
    "Bachelor of Engineering of Information Technology (Major: Computer Engineering)":{
      "Semester 1": [
        {"subject":"Calculus 1", "credit":4},
        {"subject":"Physical Training 1", "credit":0},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Introduction to Computing", "credit":3},
        {"subject":"C/C++ Programming", "credit":4}
      ],
      "Semester 2": [
        {"subject":"Discrete Mathematics", "credit":3},
        {"subject":"Digital Logic Design", "credit":3},
        {"subject":"Digital Logic Design Laboratory", "credit":1},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Object-Oriented Programming", "credit":4},
        {"subject":"Physics 1", "credit":2}
      ],
      "Semester 3": [
        {"subject":"Linear algebra", "credit":3},
        {"subject":"Calculus 2", "credit":4},
        {"subject":"Algorithms and Data Structures", "credit":4},
        {"subject":"Principle of Electrical Engineering I", "credit":3},
        {"subject":"Marxist - Leninist Political Economy", "credit":2},
        {"subject":"Principle of Electrical Engineering I Laboratory", "credit":1},
        {"subject":"Philosophy Marx - Lenin", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Computer Architecture", "credit":4},
        {"subject":"Computer Networks", "credit":4},
        {"subject":"Electronic Devices", "credit":3},
        {"subject":"Probability, Statistic & Random Process", "credit":3},
        {"subject":"Scientific Socialism", "credit":2},
        {"subject":"Electronic Devices Laboratory", "credit":1}
      ],
      "Semester 5": [
        {"subject":"Operating System", "credit":4},
        {"subject":"Principles of Database Management", "credit":4},
        {"subject":"Micro-processing Systems", "credit":3},
        {"subject":"Physical Training 2", "credit":0},
        {"subject":"Physics 3", "credit":3},
        {"subject":"Physics 3 Laboratory", "credit":1},
        {"subject":"Micro-processing Systems Laboratory", "credit":1}
      ],
      "Semester 6": [
        {"subject":"Elective 1", "credit":4},
        {"subject":"Digital System Design", "credit":3},
        {"subject":"Digital System Design Laboratory", "credit":1},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Ho Chi Minh's Thoughts", "credit":2},
        {"subject":"Embedded Systems", "credit":4},
        {"subject":"Embedded Systems Laboratory", "credit":1}
      ],
      "Summer Semester": [
        {"subject":"Internship for engineers", "credit":7}
      ],
      "Semester 7": [
        {"subject":"Elective 2", "credit":4},
        {"subject":"Concepts in VLSI Design", "credit":4},
        {"subject":"Concepts in VLSI Design Laboratory", "credit":1},
        {"subject":"Digital Signal Processing", "credit":4},
        {"subject":"Artificial intelligence", "credit":4}
      ],
      "Semester 8": [
        {"subject":"Special Study of the Field", "credit":3},
        {"subject":"Internet of Things", "credit":4},
        {"subject":"Entrepreneurship", "credit":3},
        {"subject":"Engineering Ethics and Professional Skills", "credit":3}
      ],
      "Semester 9": [
        {"subject":"Thesis", "credit":10},
        {"subject":"General Law", "credit":3}
      ]
    },
    "Bachelor of Engineering of Information Technology (Major: Network Engineering)":{
      "Semester 1": [
        {"subject":"Calculus 1", "credit":4},
        {"subject":"Physical Training 1", "credit":0},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Introduction to Computing", "credit":3},
        {"subject":"C/C++ Programming", "credit":4}
      ],
      "Semester 2": [
        {"subject":"Discrete Mathematics", "credit":3},
        {"subject":"Digital Logic Design", "credit":3},
        {"subject":"Digital Logic Design Laboratory", "credit":1},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Object-Oriented Programming", "credit":4},
        {"subject":"Physics 1", "credit":2}
      ],
      "Semester 3": [
        {"subject":"Linear algebra", "credit":3},
        {"subject":"Calculus 2", "credit":4},
        {"subject":"Algorithms and Data Structures", "credit":4},
        {"subject":"Principle of Electrical Engineering I", "credit":3},
        {"subject":"Marxist - Leninist Political Economy", "credit":2},
        {"subject":"Principle of Electrical Engineering I Laboratory", "credit":1},
        {"subject":"Philosophy Marx - Lenin", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Computer Architecture", "credit":4},
        {"subject":"Computer Networks", "credit":4},
        {"subject":"Web Application Development", "credit":3},
        {"subject":"Probability, Statistic & Random Process", "credit":3},
        {"subject":"Scientific Socialism", "credit":2}
      ],
      "Semester 5": [
        {"subject":"Operating System", "credit":4},
        {"subject":"Net-Centric Programming", "credit":4},
        {"subject":"System & Network Administration", "credit":3},
        {"subject":"Physical Training 2", "credit":0},
        {"subject":"Physics 3", "credit":3},
        {"subject":"Physics 3 Laboratory", "credit":1}
      ],
      "Semester 6": [
        {"subject":"Elective 1", "credit":4},
        {"subject":"Information System Management", "credit":4},
        {"subject":"System and Network Security", "credit":4},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Ho Chi Minh's Thoughts", "credit":2}
      ],
      "Summer Semester": [
        {"subject":"Internship for engineers", "credit":7}
      ],
      "Semester 7": [
        {"subject":"Elective 2", "credit":4},
        {"subject":"Entrepreneurship", "credit":3},
        {"subject":"Scalable and Distributed Computing", "credit":4},
        {"subject":"Artificial intelligence", "credit":4}
      ],
      "Semester 8": [
        {"subject":"Elective 3", "credit":4},
        {"subject":"Internet of Things", "credit":4},
        {"subject":"Special Study of the Field", "credit":3},
        {"subject":"Engineering Ethics and Professional Skills", "credit":3}
      ],
      "Semester 9": [
        {"subject":"Thesis", "credit":10},
        {"subject":"General Law", "credit":3}
      ]
    },
    "Bachelor of Science in Computer Science":{
      "Semester 1": [
        {"subject":"Calculus 1", "credit":4},
        {"subject":"Physics 1", "credit":3},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Introduction to Computing", "credit":3},
        {"subject":"C/C++ Programming", "credit":4}
      ],
      "Semester 2": [
        {"subject":"Discrete Mathematics", "credit":3},
        {"subject":"Physics 3 Laboratory", "credit":1},
        {"subject":"Computer Networks", "credit":4},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Object-Oriented Programming", "credit":4},
        {"subject":"Physics 3", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Linear algebra", "credit":3},
        {"subject":"Calculus 2", "credit":4},
        {"subject":"Algorithms and Data Structures", "credit":4},
        {"subject":"Principle of Electrical Engineering I", "credit":3},
        {"subject":"Marxist - Leninist Political Economy", "credit":2},
        {"subject":"Principle of Electrical Engineering I Laboratory", "credit":1},
        {"subject":"Philosophy Marx - Lenin", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Computer Architecture", "credit":4},
        {"subject":"Physical Training 1", "credit":0},
        {"subject":"Elective 1", "credit":4},
        {"subject":"Object-Oriented Analysis and Design", "credit":4},
        {"subject":"Web Application Development", "credit":4}
      ],
      "Semester 5": [
        {"subject":"Probability, Statistic & Random Process", "credit":3},
        {"subject":"Scientific Socialism", "credit":2},
        {"subject":"Principles of Programming Languages", "credit":4},
        {"subject":"Physical Training 2", "credit":0},
        {"subject":"Elective 2", "credit":4},
        {"subject":"Elective 3", "credit":4}
      ],
      "Semester 6": [
        {"subject":"Software Engineering", "credit":4},
        {"subject":"Artificial Intelligence", "credit":4},
        {"subject":"General law", "credit":3},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Free elective", "credit":3},
        {"subject":"Entrepreneurship", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Operating Systems", "credit":4},
        {"subject":"Ho Chi Minh's Thoughts", "credit":2},
        {"subject":"Special Study of the Field", "credit":3}
      ],
      "Semester 8": [
        {"subject":"Thesis", "credit":10}
      ]
    },
    "Bachelor of Science in Data Science":{
      "Semester 1": [
        {"subject":"Calculus 1", "credit":4},
        {"subject":"Fundamentals of Programming", "credit":4},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Introduction to Data Science", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Probability, Statistic & Random Process", "credit":2},
        {"subject":"Linear Algebra", "credit":3},
        {"subject":"Philosophy Marx -Lenin", "credit":4},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Object-Oriented Programming", "credit":4}
      ],
      "Semester 3": [
        {"subject":"Statistical Method", "credit":3},
        {"subject":"Data Structures and Algorithms", "credit":4},
        {"subject":"Principles of Database Management", "credit":4},
        {"subject":"Fundamental Concepts of Data Security", "credit":4},
        {"subject":"Marxist - Leninist Political Economy", "credit":2}
      ],
      "Semester 4": [
        {"subject":"Scientific Socialism", "credit":2},
        {"subject":"Physical Training 1", "credit":0},
        {"subject":"General law", "credit":3},
        {"subject":"Artificial Intelligence", "credit":4},
        {"subject":"Statistical Learningt", "credit":4},
        {"subject":"Regression Analysis", "credit":4}
      ],
      "Semester 5": [
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Data Science and Data Visualization", "credit":4},
        {"subject":"Data Mining", "credit":4},
        {"subject":"Scalable and Distributed Computing", "credit":4},
        {"subject":"Data Analysis", "credit":4}
      ],
      "Semester 6": [
        {"subject":"Ho Chi Minh's Thoughts", "credit":2},
        {"subject":"Machine Learning", "credit":4},
        {"subject":"Deep Learning", "credit":4},
        {"subject":"Elective", "credit":4},
        {"subject":"Elective", "credit":4}
      ],
      "Summer Semester": [
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Elective 3", "credit":4},
        {"subject":"Internet of Things", "credit":4},
        {"subject":"FEngineering Ethics and Professional Skills", "credit":3},
        {"subject":"Special Study of the Field", "credit":3}
      ],
      "Semester 8": [
        {"subject":"Thesis", "credit":10}
      ]
    }
  }, 
  "School of Business":{
    "Bachelor of Business Management":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Philosophy of Marxism and Leninism", "credit":3},
        {"subject":"Physical Training 1", "credit":0}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Political economics of Marxism and Leninism", "credit":2},
        {"subject":"Physical Training 2", "credit":0},
        {"subject":"Critical Thinking", "credit":3},
        {"subject":"Scientific Socialism", "credit":2}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":4},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":2},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"Ho Chi Minh’s Thoughts", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Ethics", "credit":4},
        {"subject":"Business Law", "credit":3},
        {"subject":"Strategy Formulation and Implementation", "credit":2},
        {"subject":"Production and Operations Management", "credit":2},
        {"subject":"Elective 1", "credit":3},
        {"subject":"Elective course", "credit":4}
      ],
      "Semester 6": [
        {"subject":"Quality Management", "credit":4},
        {"subject":"Business Communication", "credit":3},
        {"subject":"Entrepreneurship and Small Business Management", "credit":2},
        {"subject":"Human Resource Management", "credit":2},
        {"subject":"Internship", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Logistic and Supply Chain Management", "credit":4},
        {"subject":"Project Management", "credit":3},
        {"subject":"Business Research Methods", "credit":2},
        {"subject":"Workshop 2 on Business Management", "credit":2},
        {"subject":"Elective 2", "credit":3},
        {"subject":"Elective 3", "credit":4}
      ],
      "Semester 8": [
        {"subject":"Thesis ", "credit":4}
      ]
    },
    "Bachelor of International Business":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Philosophy of Marxism and Leninism", "credit":3},
        {"subject":"Physical Training 1", "credit":0}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Political economics of Marxism and Leninism", "credit":2},
        {"subject":"Physical Training 2", "credit":2},
        {"subject":"Critical Thinking", "credit":3},
        {"subject":"Scientific Socialism", "credit":2}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"International Economics ", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"Ho Chi Minh’s Thoughts", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Strategy Formulation and Implementation", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Elective 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 6": [
        {"subject":"International Financial Management", "credit":3},
        {"subject":"Business Communication", "credit":3},
        {"subject":"International Business Management", "credit":3},
        {"subject":"Elective 2", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Import Export Management", "credit":3},
        {"subject":"International Marketing", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Workshop 2 on International Business", "credit":2},
        {"subject":"Elective 3", "credit":3},
        {"subject":"Elective 4", "credit":3}
      ],
      "Semester 8": [
        {"subject":"Thesis", "credit":10}
      ]
    },
    "Bachelor of Marketing":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Philosophy of Marxism and Leninism", "credit":3},
        {"subject":"Physical Training 1", "credit":0}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Political economics of Marxism and Leninism", "credit":2},
        {"subject":"Critical Thinking", "credit":3},
        {"subject":"Scientific Socialism", "credit":2},
        {"subject":"Physical Training 2", "credit":0}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"Ho Chi Minh's Thoughts", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Business Communication", "credit":3},
        {"subject":"Strategy Formulation and Implementation", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Elective 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Business Law", "credit":3},
        {"subject":"Marketing Research", "credit":3},
        {"subject":"Consumer Behavior", "credit":3},
        {"subject":"Elective 2", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Marketing Strategy", "credit":3},
        {"subject":"International Marketing", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Workshop 2 on Marketing", "credit":2},
        {"subject":"Elective 3", "credit":3},
        {"subject":"Elective 4", "credit":3}
      ],
      "Semester 8": [
        {"subject":"Thesis", "credit":10}
      ]
    },
    "Bachelor of Hospitality Management":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Philosophy of Marxism and Leninism", "credit":3},
        {"subject":"Physical Training 1", "credit":0}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Political economics of Marxism and Leninism", "credit":2},
        {"subject":"Critical Thinking", "credit":3},
        {"subject":"Scientific Socialism", "credit":2},
        {"subject":"Physical Training 2", "credit":0}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"History of Vietnamese Communist Party", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"Ho Chi Minh's Thoughts", "credit":2},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Introduction to Hospitality Industry", "credit":3},
        {"subject":"Food and Beverage Management", "credit":3},
        {"subject":"Leadership and Management Skills in Hospitality Industry", "credit":3},
        {"subject":"Hospitality Legal Issues", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Housekeeping Operations & Management", "credit":3},
        {"subject":"Business Communication", "credit":3},
        {"subject":"The Professional Waiter", "credit":3},
        {"subject":"Human Resources Management", "credit":3},
        {"subject":"Front Office Management and Operations", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Hospitality Sales and Marketing", "credit":3},
        {"subject":"Hotel Management and Operations", "credit":3},
        {"subject":"Workshop 2 on Hospitality Management", "credit":2},
        {"subject":"Elective 1", "credit":3},
        {"subject":"Elective 2", "credit":3}
      ],
      "Semester 8": [
        {"subject":"Thesis", "credit":10}
      ]
    },
    "University of New South Wales (2+2)":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"Introduction to Psychology", "credit":3},
        {"subject":"Management Information Systems", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Elective course", "credit":3}
      ]
    },
    "Auckland University of Technology (1+2)":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3},
        {"subject":"World Economic Geography", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Introduction to Macroeconomics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective 1", "credit":3},
        {"subject":"Elective 2", "credit":3},
        {"subject":"Elective course", "credit":3}
      ]
    },
    "Auckland University of Technology (1.5+2.5)":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Introduction to Macroeconomics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"World Economic Geography", "credit":3}
      ]
    },
    "University of West of England (2+2)":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Microeconomics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macroeconomics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ]
    },
    "University of West of England (4+0)-Business and human resource management":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Micro Economics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Elective course", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Communication", "credit":3},
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Logistics and Supply Chain Management", "credit":3},
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Quality Management", "credit":3},
        {"subject":"Project Management", "credit":3},
        {"subject":"Entrepreneurship and Small Business Management", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Business Project in Theory", "credit":4},
        {"subject":"Strategy and Human Resource Management", "credit":4},
        {"subject":"Academic and Professional Development", "credit":4},
        {"subject":"International Human Resource Management", "credit":4}
      ],
      "Semester 8": [
        {"subject":"Business Project", "credit":4},
        {"subject":"Strategy and Human Resource Management", "credit":4},
        {"subject":"Human Resource Development and Knowledge Management", "credit":4},
        {"subject":"Managing Organizational Performance", "credit":4}
      ]
    },
    "University of West of England (4+0)-Business and management":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Micro Economics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Elective course", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Communication", "credit":3},
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Logistics and Supply Chain Management", "credit":3},
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Quality Management", "credit":3},
        {"subject":"Project Management", "credit":3},
        {"subject":"Entrepreneurship and Small Business Management", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject":"Business Project in Theory", "credit":4},
        {"subject":"Business Strategy", "credit":4},
        {"subject":"Academic and Professional Development", "credit":4},
        {"subject":"Managing Organizational Change", "credit":4}
      ],
      "Semester 8": [
        {"subject":"Business Project", "credit":4},
        {"subject":"Global Marketing Management", "credit":4},
        {"subject":"Sustainable Business", "credit":4},
        {"subject":"Integrated Business Management Simulation", "credit":4}
      ]
    },
    "University of West of England (4+0)-Business management with marketing":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Micro Economics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Elective course", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Communication", "credit":3},
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Logistics and Supply Chain Management", "credit":3},
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Quality Management", "credit":3},
        {"subject":"Project Management", "credit":3},
        {"subject":"Entrepreneurship and Small Business Management", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject": "Business Project in Theory", "credit": 4},
        {"subject": "Business Strategy", "credit": 4},
        {"subject": "Academic and Professional Development", "credit": 4},
        {"subject": "Managing Organizational Change", "credit": 4}
      ],
      "Semester 8": [
        {"subject": "Business Project", "credit": 4},
        {"subject": "Marketing Service", "credit": 4},
        {"subject": "Global Marketing Management", "credit": 4},
        {"subject": "Integrated Business Management Simulation", "credit": 4}
      ]
    },
    "University of West of England (4+0)-Business and events management":{
      "Semester 1": [
        {"subject":"Writing AE1", "credit":2},
        {"subject":"Listening AE1", "credit":2},
        {"subject":"Financial Accounting", "credit":3},
        {"subject":"Introduction to Business Administration", "credit":3},
        {"subject":"Introduction to Micro Economics", "credit":3},
        {"subject":"Business Computing Skills", "credit":3}
      ],
      "Semester 2": [
        {"subject":"Writing AE2", "credit":2},
        {"subject":"Speaking AE2", "credit":2},
        {"subject":"Introduction to Macro Economics", "credit":3},
        {"subject":"Principles of Management", "credit":3},
        {"subject":"Math for Business", "credit":4},
        {"subject":"Critical Thinking", "credit":3}
      ],
      "Semester 3": [
        {"subject":"Principles of Marketing", "credit":3},
        {"subject":"Statistics for Business", "credit":3},
        {"subject":"General Law", "credit":3},
        {"subject":"Elective course", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 4": [
        {"subject":"Fundamental of Financial Management", "credit":3},
        {"subject":"International Economics", "credit":3},
        {"subject":"Business Law", "credit":3},
        {"subject":"Organizational Behavior", "credit":3},
        {"subject":"Quantitative Methods for Business", "credit":3},
        {"subject":"Workshop 1", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Semester 5": [
        {"subject":"Business Communication", "credit":3},
        {"subject":"Business Ethics", "credit":3},
        {"subject":"Production and Operations Management", "credit":3},
        {"subject":"Logistics and Supply Chain Management", "credit":3},
        {"subject":"Specialized Internship", "credit":3}
      ],
      "Semester 6": [
        {"subject":"Quality Management", "credit":3},
        {"subject":"Project Management", "credit":3},
        {"subject":"Entrepreneurship and Small Business Management", "credit":3},
        {"subject":"Business Research Methods", "credit":3},
        {"subject":"Elective course", "credit":3}
      ],
      "Summer Semester": [
        {"subject":"Specialized Internship", "credit":3},
        {"subject":"Internship", "credit":3}
      ],
      "Semester 7": [
        {"subject": "Business Project in Theory", "credit": 4},
        {"subject": "Business Strategy", "credit": 4},
        {"subject": "Academic and Professional Development", "credit": 4},
        {"subject": "Specialized Events Practice", "credit": 4}
      ],
      "Semester 8": [
        {"subject": "Business Project", "credit": 4},
        {"subject": "Marketing Service", "credit": 4},
        {"subject": "Corporate Events", "credit": 4},
        {"subject": "Contemporary Issues in Events", "credit": 4}
      ]
    },
    "University of Nottingham (2+2)":{
      "Semester 1": [
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Introduction to Business Administration", "credit": 3},
        {"subject": "Introduction to Microeconomics", "credit": 3},
        {"subject": "Business Computing Skills", "credit": 3}
      ],
      "Semester 2": [
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Introduction to Macro Economics", "credit": 3},
        {"subject": "Principles of Management", "credit": 3},
        {"subject": "Financial Accounting", "credit": 3},
        {"subject": "Math for Business", "credit": 4}
      ],
      "Semester 3": [
        {"subject": "Fundamental of Financial Management", "credit": 3},
        {"subject": "Principles of Marketing", "credit": 3},
        {"subject": "Statistics for Business", "credit": 3},
        {"subject": "Strategy Formulation and Implementation", "credit": 3},
        {"subject": "Elective course", "credit": 3},
        {"subject": "Elective course", "credit": 3}
      ],
      "Semester 4": [
        {"subject": "Organizational Behavior", "credit": 3},
        {"subject": "Business Communication", "credit": 3},
        {"subject": "International Economics", "credit": 3},
        {"subject": "Managerial Accounting", "credit": 3},
        {"subject": "Entrepreneurship and Small Business Management", "credit": 3},
        {"subject": "Quantitative Methods for Business", "credit": 3},
        {"subject": "Workshop 1", "credit": 3}
      ]
    },
    "University of Houston (2+2)":{
      "Semester 1": [
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Introduction to Microeconomics", "credit": 3},
        {"subject": "Business Computing Skills", "credit": 3},
        {"subject": "Critical Thinking", "credit": 3}
      ],
      "Semester 2": [
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Introduction to Macroeconomics", "credit": 3},
        {"subject": "Principles of Management", "credit": 3},
        {"subject": "Math for Business", "credit": 4},
        {"subject": "Biology", "credit": 4}
      ],
      "Semester 3": [
        {"subject": "Principles of Marketing", "credit": 3},
        {"subject": "Financial Accounting", "credit": 3},
        {"subject": "Statistics for Business", "credit": 3},
        {"subject": "Introduction to Sociology", "credit": 3},
        {"subject": "Business Ethics", "credit": 3}
      ],
      "Semester 4": [
        {"subject": "Managerial Accounting", "credit": 3},
        {"subject": "Fundamental of Financial Management", "credit": 3},
        {"subject": "Production and Operations Management", "credit": 3},
        {"subject": "Vietnamese History and Culture", "credit": 3}
      ]
    },
    "University of West of England (3+1)":{
      "Semester 1": [
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Financial Accounting", "credit": 3},
        {"subject": "Introduction to Business Administration", "credit": 3},
        {"subject": "Introduction to Microeconomics", "credit": 3},
        {"subject": "Business Computing Skills", "credit": 3}
      ],
      "Semester 2": [
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Introduction to Macroeconomics", "credit": 3},
        {"subject": "Principles of Management", "credit": 3},
        {"subject": "Math for Business", "credit": 4},
        {"subject": "Critical Thinking", "credit": 3}
      ],
      "Semester 3": [
        {"subject": "Statistics for Business", "credit": 3},
        {"subject": "Principles of Marketing", "credit": 3},
        {"subject": "General Law", "credit": 3},
        {"subject": "Elective course 1", "credit": 3},
        {"subject": "Elective course 2", "credit": 3}
      ],
      "Semester 4": [
        {"subject": "Fundamental of Financial Management", "credit": 3},
        {"subject": "International Economics", "credit": 3},
        {"subject": "Business Law", "credit": 3},
        {"subject": "Organizational Behavior", "credit": 3},
        {"subject": "Quantitative Methods for Business", "credit": 3},
        {"subject": "Workshop 1", "credit": 3},
        {"subject": "Elective course", "credit": 3}
      ],
      "Semester 5": [
        {"subject": "Business Communication", "credit": 3},
        {"subject": "Business Ethics", "credit": 3},
        {"subject": "Logistics and Supply Chain Management", "credit": 3},
        {"subject": "Production and Operations Management", "credit": 3}
      ],
      "Semester 6": [
        {"subject": "Quality Management", "credit": 3},
        {"subject": "Project Management", "credit": 3},
        {"subject": "Entrepreneurship and Small Business Management", "credit": 3},
        {"subject": "Business Research Methods", "credit": 3}
      ],
      "Summer Semester": [
        {"subject": "Internship", "credit": 3},
        {"subject": "Specialized Internship", "credit": 3}
      ]
    },
    "Lakehead University (2+2)":{
      "Semester 1": [
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Principles of Marketing", "credit": 3},
        {"subject": "Financial Accounting", "credit": 3},
        {"subject": "Introduction to Microeconomics", "credit": 3}
      ],
      "Semester 2": [
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Managerial Accounting", "credit": 3},
        {"subject": "Introduction to Macro Economics", "credit": 3},
        {"subject": "Principles of Management", "credit": 3}
      ],
      "Semester 3": [
        {"subject": "Business Communications", "credit": 3},
        {"subject": "Fundamental of Financial Management", "credit": 3},
        {"subject": "Statistics for Business", "credit": 3},
        {"subject": "Marketing Strategy", "credit": 3},
        {"subject": "Quantitative Methods for Business", "credit": 3},
        {"subject": "Management Information Systems", "credit": 3}
      ],
      "Semester 4": [
        {"subject": "Logistics and Supply Chain Management", "credit": 3},
        {"subject": "Corporate Finance", "credit": 3},
        {"subject": "Organizational Behaviour", "credit": 3},
        {"subject": "Human Resources Management", "credit": 3},
        {"subject": "Production and Operations Management", "credit": 3}
      ]
    },
    "Sydney University (2+2)":{
      "Semester 1": [
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Financial Accounting", "credit": 3},
        {"subject": "Introduction to Microeconomics", "credit": 3},
        {"subject": "Critical Thinking", "credit": 3}
      ],
      "Semester 2": [
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Principles of Marketing", "credit": 3},
        {"subject": "Introduction to Macro Economics", "credit": 3}
      ],
      "Semester 3": [
        {"subject": "Fundamental of Financial Management", "credit": 3},
        {"subject": "Statistics for Business", "credit": 3},
        {"subject": "Principles of Management", "credit": 3},
        {"subject": "Organizational Behaviour", "credit": 3},
        {"subject": "Math for Business", "credit": 4}
      ],
      "Semester 4": [
        {"subject": "Quantitative Methods of Business", "credit": 3},
        {"subject": "International Economics", "credit": 3},
        {"subject":"Elective course", "credit":3}
      ]
    }
  }, 
  "Department of Biotechnology": {
    "Biotechnology Program": {
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Biology", "credit": 3 },
        { "subject": "Practice in Biology", "credit": 1 },
        { "subject": "Chemistry for Engineering", "credit": 3 },
        { "subject": "Academic English 1", "credit": 4 },
        { "subject": "Physical Training 1", "credit": 0}
      ],
      "Semester 2": [
        { "subject": "General Law", "credit": 3 },
        { "subject": "Physics for Biology", "credit": 2 },
        { "subject": "Academic English 2", "credit": 4 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Introduction to Biotechnology", "credit": 2 },
        { "subject": "Physical Training 2", "credit": 0}
      ],
      "Summer Semester": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political economics of Marxism and Leninism", "credit": 2 },
        { "subject": "Environmental Science", "credit": 3 }
      ],
      "Semester 3": [
        { "subject": "Genetics", "credit": 3 },
        { "subject": "Practice in Genetics", "credit": 1 },
        { "subject": "Plant Physiology", "credit": 3 },
        { "subject": "Analytical Chemistry", "credit": 3 },
        { "subject": "Practice in Analytical Chemistry", "credit": 1 },
        { "subject": "Scientific Socialism", "credit": 2 }
      ],
      "Semester 4": [
        { "subject": "Biostatistics", "credit": 2 },
        { "subject": "Practice in Biostatistics", "credit": 1 },
        { "subject": "Biochemistry", "credit": 3 },
        { "subject": "Practice in Biochemistry", "credit": 1 },
        { "subject": "Microbiology", "credit": 3 },
        { "subject": "Practice in Microbiology", "credit": 1 },
        { "subject": "Cell Biology", "credit": 3 },
        { "subject": "Human Physiology", "credit": 3 }
      ],
      "Semester 5": [
        { "subject": "History of Vietnamese Communist Party", "credit": 2 },
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "Molecular Biotechnology", "credit": 3 },
        { "subject": "Practice in Molecular Biotechnology", "credit": 1 },
        { "subject": "Immunology", "credit": 3 },
        { "subject": "Practice in Immunology", "credit": 1 },
        { "subject": "Foundation Electives", "credit": 6 }
      ],
      "Semester 6": [
        { "subject": "Bioprocess Engineering", "credit": 3 },
        { "subject": "Practice in Bioprocess Engineering", "credit": 1 },
        { "subject": "Bioinformatics", "credit": 3 },
        { "subject": "Practice in Bioinformatics", "credit": 1 },
        { "subject": "Foundation Electives", "credit": 6 },
        { "subject": "Free Electives", "credit": 6 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship", "credit": 2 }
      ],
      "Semester 7": [
        { "subject": "Experimental Design", "credit": 3 },
        { "subject": "Professional Electives", "credit": 16 }
      ],
      "Semester 8": [
        { "subject": "Thesis", "credit": 12 }
      ]
    },
    "Biochemistry Program":{
            "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Biology", "credit": 3 },
        { "subject": "Practice in Biology", "credit": 1 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Academic English 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0}
      ],
      "Semester 2": [
        { "subject": "Academic English 2", "credit": 4 },
        { "subject": "Biostatistics", "credit": 2 },
        { "subject": "Practice in Biostatistics", "credit": 1 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Inorganic Chemistry", "credit": 3 },
        { "subject": "Inorganic Chemistry Lab", "credit": 1 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Introduction to Biochemistry", "credit": 2 },
        { "subject": "Physical Training 2", "credit": 0}
      ],
      "Summer Semester": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "General Law", "credit": 3 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Biochemistry 1", "credit": 3 },
        { "subject": "Molecular Cell Biology", "credit": 3 },
        { "subject": "Molecular Cell Biology Lab", "credit": 1 },
        { "subject": "Experimental Design and Technical Communication", "credit": 3 },
        { "subject": "Organic Chemistry 1", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Organic Chemistry Lab", "credit": 2 },
        { "subject": "Biochemistry 2", "credit": 3 },
        { "subject": "Biochemistry 2 Lab", "credit": 2 },
        { "subject": "Fundamentals of Analytical Chemistry", "credit": 3 },
        { "subject": "Fundamentals in Analytical Chemistry Lab", "credit": 1 },
        { "subject": "Organic Chemistry 2", "credit": 3 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 }
      ],
      "Semester 5": [
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "Bioinformatics", "credit": 3 },
        { "subject": "Practice in Bioinformatics", "credit": 1 },
        { "subject": "Biophysical Chemistry", "credit": 3 },
        { "subject": "Instrumental Analysis", "credit": 3 },
        { "subject": "Instrumental Analysis Lab", "credit": 1 },
        { "subject": "Environmental Science", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Microbiology", "credit": 3 },
        { "subject": "Practice in Microbiology", "credit": 1 },
        { "subject": "Methods in Biochemistry", "credit": 3 },
        { "subject": "Methods in Biochemistry Lab", "credit": 2 },
        { "subject": "Enzymology", "credit": 3 },
        { "subject": "Enzymology Lab", "credit": 1 },
        { "subject": "Free Elective", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship", "credit": 2 }
      ],
      "Semester 7": [
        { "subject": "Biopharmaceutics", "credit": 3 },
        { "subject": "Physical Chemistry", "credit": 3 },
        { "subject": "Professional Electives", "credit": 12 }
      ],
      "Semester 8": [
        { "subject": "Thesis", "credit": 12 }
      ]
    },
    "Food Technology Program": {
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Biology", "credit": 3 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Academic English 1", "credit": 4 },
        { "subject": "Physical Training 1", "credit": 0}
      ],
      "Semester 2": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "General Law", "credit": 3 },
        { "subject": "Organic Chemistry", "credit": 3 },
        { "subject": "Academic English 2", "credit": 4 },
        { "subject": "Physical Training 2", "credit": 0}
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Introduction to Food Science and Technology", "credit": 3 },
        { "subject": "Food Engineering Principles", "credit": 4 },
        { "subject": "Food Chemistry and Biochemistry", "credit": 3 },
        { "subject": "Biostatistics", "credit": 2 },
        { "subject": "Practice in Biostatistics", "credit": 1 },
        { "subject": "Food Sustainability", "credit": 2 }
      ],
      "Semester 4": [
        { "subject": "Food Microbiology", "credit": 3 },
        { "subject": "Practice in Food Microbiology", "credit": 1 },
        { "subject": "Nutrition and Functional Foods", "credit": 3 },
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 },
        { "subject": "Food Unit Operations 1", "credit": 3 },
        { "subject": "Practice in Food Unit Operations 1", "credit": 1 },
        { "subject": "Free Elective", "credit": 3 }
      ],
      "Semester 5": [
        { "subject": "Food Physics and Colloids", "credit": 3 },
        { "subject": "Food Analysis", "credit": 3 },
        { "subject": "Practice in Food Analysis", "credit": 1 },
        { "subject": "Enzyme and Food Fermentation", "credit": 3 },
        { "subject": "Practice in Enzyme and Food Fermentation", "credit": 1 },
        { "subject": "Toxicology and Food Safety", "credit": 3 },
        { "subject": "Food Packaging and Food Additives", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Food Unit Operations 2", "credit": 3 },
        { "subject": "Practice in Food Unit Operations 2", "credit": 1 },
        { "subject": "Food Quality Assurance System", "credit": 3 },
        { "subject": "Food Microbiology Analysis", "credit": 2 },
        { "subject": "Practice in Food Microbiology Analysis", "credit": 1 },
        { "subject": "Food Sensory Analysis", "credit": 2 },
        { "subject": "Practice in Food Sensory Analysis", "credit": 1 },
        { "subject": "Free Elective", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 1", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Food Product Development and Marketing", "credit": 2 },
        { "subject": "Practice in Food Product Development and Marketing", "credit": 1 },
        { "subject": "Scientific Writing and Design of Experiments", "credit": 3 },
        { "subject": "Post-harvest Technologies", "credit": 3 },
        { "subject": "Food Laws and Standards", "credit": 2 },
        { "subject": "Food Plant Design", "credit": 3 }
      ],
      "Semester 8": [
        { "subject": "Internship 2", "credit": 3 },
        { "subject": "Major Electives", "credit": 12 }
      ],
      "Semester 9": [
        { "subject": "Thesis", "credit": 12 }
      ]
    }
  }, 
  "School of Chemical & Environmental Engineering": {
    "Bachelor of Chemical Engineering":{
      "Semester 1": [
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 },
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Biology", "credit": 3 },
        { "subject": "Practice in Biology", "credit": 1 },
        { "subject": "Engineering Drawing", "credit": 3 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Applied Fluid Mechanics", "credit": 2 },
        { "subject": "Applied Fluid Mechanics Lab", "credit": 1 }
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Physics 2 - Thermodynamics", "credit": 2 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 }
      ],
      "Semester 3": [
        { "subject": "Inorganic Chemistry", "credit": 3 },
        { "subject": "Inorganic Chemistry Lab", "credit": 1 },
        { "subject": "Applied Mechanics", "credit": 2 },
        { "subject": "Organic Chemistry 1", "credit": 3 },
        { "subject": "Industrial Chemistry", "credit": 2 },
        { "subject": "Analytical Chemistry 1", "credit": 3 },
        { "subject": "Calculus 2", "credit": 4 }
      ],
      "Semester 4": [
        { "subject": "Physical Chemistry 1", "credit": 3 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Reaction Kinetics and Catalysis", "credit": 3 },
        { "subject": "Applied Statistics", "credit": 3 },
        { "subject": "Introduction to Chemical Engineering", "credit": 2 },
        { "subject": "Principles of EE1", "credit": 3 },
        { "subject": "Physical Chemistry 2", "credit": 2 },
        { "subject": "Physical Chemistry 2 Lab", "credit": 1 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Military Education", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Biochemistry", "credit": 3 },
        { "subject": "Biochemistry Lab", "credit": 1 },
        { "subject": "Programming for Engineers", "credit": 3 },
        { "subject": "Programming for Engineers Lab", "credit": 1 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 },
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "Computational Chemistry", "credit": 2 },
        { "subject": "Computational Chemistry Lab", "credit": 1 },
        { "subject": "Chemical Reaction Engineering", "credit": 3 },
        { "subject": "Organic Chemistry 2", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Analytical Chemistry 2", "credit": 3 },
        { "subject": "Analytical Chemistry Laboratory", "credit": 2 },
        { "subject": "Organic Chemistry Laboratory", "credit": 2 },
        { "subject": "Process Instrumentation and Control", "credit": 2 },
        { "subject": "Engineering Ethics and Professional Skills", "credit": 3 },
        { "subject": "Simulation and Optimization", "credit": 2 },
        { "subject": "Simulation and Optimization Lab", "credit": 1 },
        { "subject": "Research Methodology", "credit": 3 },
        { "subject": "Introduction to Health Safety and Environment", "credit": 1 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Research 1", "credit": 1 },
        { "subject": "Internship", "credit": 2 }
      ],
      "Semester 7": [
        { "subject": "Mass Transfer Operations", "credit": 3 },
        { "subject": "Heat Transfer Operations", "credit": 3 },
        { "subject": "Mechanical Unit Operations", "credit": 3 }
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Bachelor of Environment Engineering":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Lab", "credit": 1 },
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "General Law", "credit": 3 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Engineering Ethics and Professional Skills", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 }
      ],
      "Semester 3": [
        { "subject": "Introduction to Computing", "credit": 3 },
        { "subject": "Fundamental of Analytical Chemistry", "credit": 2 },
        { "subject": "Fundamental of Analytical Chemistry Lab", "credit": 1 },
        { "subject": "Biochemistry", "credit": 3 },
        { "subject": "Biochemistry Lab", "credit": 1 },
        { "subject": "Engineering Drawing", "credit": 2 },
        { "subject": "Engineering Drawing Lab", "credit": 1 },
        { "subject": "Mechanics of Materials", "credit": 2 },
        { "subject": "Environmental Ecology", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Introduction to Environmental Engineering", "credit": 3 },
        { "subject": "Environmental Microbiology", "credit": 2 },
        { "subject": "Environmental Microbiology Lab", "credit": 2 },
        { "subject": "Environmental Chemistry 1", "credit": 2 },
        { "subject": "Environmental Chemistry 1 Lab", "credit": 2 },
        { "subject": "Environmental Chemistry 2", "credit": 2 },
        { "subject": "Environmental Chemistry 2 Lab", "credit": 2 },
        { "subject": "Applied Statistics", "credit": 2 },
        { "subject": "Applied Statistics Lab", "credit": 1 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Military Education", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Hydraulics for Environmental Engineering", "credit": 2 },
        { "subject": "Hydraulics for Environmental Engineering Lab", "credit": 1 },
        { "subject": "Physical and Chemical Processes for Environmental Engineering", "credit": 2 },
        { "subject": "Physical and Chemical Processes Lab", "credit": 1 },
        { "subject": "Biological Processes for Environmental Engineering", "credit": 2 },
        { "subject": "Biological Processes Lab", "credit": 1 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 },
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "Internship 1", "credit": 2 },
        { "subject": "Elective (min 1)", "credit": 3 } 
      ],
      "Semester 6": [
        { "subject": "Basic Theory of Environmental Structures", "credit": 2 },
        { "subject": "Advanced Engineering Drawing", "credit": 2 },
        { "subject": "Advanced Engineering Drawing Lab", "credit": 1 },
        { "subject": "Water Treatment", "credit": 3 },
        { "subject": "Water Treatment Lab", "credit": 1 },
        { "subject": "Municipal Wastewater Treatment", "credit": 3 },
        { "subject": "Municipal Wastewater Treatment Lab", "credit": 1 },
        { "subject": "Industrial Wastewater Treatment", "credit": 2 },
        { "subject": "Industrial Wastewater Treatment Lab", "credit": 2 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 2", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Project 1", "credit": 2 },
        { "subject": "Project 2", "credit": 2 },
        { "subject": "Heat and Mass Transfer", "credit": 3 },
        { "subject": "Technical Electives (min 2)", "credit": 7 }
      ],
      "Semester 8": [
        { "subject": "Occupational Health Safety and Environment", "credit": 2 },
        { "subject": "Pre-thesis", "credit": 2 },
        { "subject": "Solid Waste and Hazardous Waste Management", "credit": 3 },
        { "subject": "Solid Waste and Hazardous Waste Management Lab", "credit": 1 },
        { "subject": "Air Pollution Control", "credit": 3 },
        { "subject": "Air Pollution Control Lab", "credit": 1 },
        { "subject": "Free Elective (min 1)", "credit": 3 }
      ],
      "Summer Semester (Year 4)": [
        { "subject": "Internship 3", "credit": 3 }
      ],
      "Semester 9": [
        { "subject": "Thesis", "credit": 10 }
      ]
    }
  }, 
  "School of Civil Engineering and Management": {
    "Bachelor of Civil Engineering":{
      "Semester 1": [
          { "subject": "Calculus 1", "credit": 4 },
          { "subject": "Physics 1", "credit": 2 },
          { "subject": "Physics 2", "credit": 2 },
          { "subject": "General Chemistry", "credit": 3 },
          { "subject": "Chemistry Laboratory", "credit": 1 },
          { "subject": "Introduction to Civil Engineering", "credit": 1 },
          { "subject": "English for Specific Purposes 1", "credit": 4 }
        ],
        "Semester 2": [
          { "subject": "Calculus 2", "credit": 4 },
          { "subject": "Engineering Mechanics - Statics", "credit": 3 },
          { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
          { "subject": "Political Economics of Marxism and Leninism", "credit": 2 },
          { "subject": "Informatics for Engineers", "credit": 3 },
          { "subject": "English for Specific Purposes 2", "credit": 4 }
        ],
        "Summer Semester 1": [
          { "subject": "Scientific Socialism", "credit": 2 },
          { "subject": "Physics 3", "credit": 3 },
          { "subject": "Physics Laboratory", "credit": 1 },
          { "subject": "Differential Equations", "credit": 4 }
        ],
        "Semester 3": [
          { "subject": "History of the Communist Party of Vietnam", "credit": 2 },
          { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
          { "subject": "CADD", "credit": 3 },
          { "subject": "CADD Practice", "credit": 1 },
          { "subject": "Strength of Materials 1", "credit": 2 },
          { "subject": "Strength of Materials Lab", "credit": 1 },
          { "subject": "Engineering Mechanics - Dynamics", "credit": 3 },
          { "subject": "Fluid Mechanics", "credit": 2 },
          { "subject": "Fluid Mechanics Lab", "credit": 1 },
          { "subject": "Linear Algebra", "credit": 2 }
        ],
        "Semester 4": [
          { "subject": "Numerical Methods", "credit": 3 },
          { "subject": "Structural Mechanics 1", "credit": 2 },
          { "subject": "Strength of Materials 2", "credit": 2 },
          { "subject": "Construction Materials", "credit": 3 },
          { "subject": "Hydrology and Hydraulics", "credit": 3 },
          { "subject": "Architecture", "credit": 2 },
          { "subject": "Analytical Thinking", "credit": 3 },
          { "subject": "Probability and Statistics", "credit": 3 }
        ],
        "Summer Semester 2": [
          { "subject": "National Defense Education", "credit": 0 }
        ],
        "Semester 5": [
          { "subject": "Soil Mechanics", "credit": 3 },
          { "subject": "Soil Mechanics Lab", "credit": 1 },
          { "subject": "Reinforced Concrete Structures 1", "credit": 3 },
          { "subject": "Steel Structures", "credit": 3 },
          { "subject": "Structural Mechanics 2", "credit": 3 },
          { "subject": "Water Supply and Drainage", "credit": 3 }
        ],
        "Semester 6": [
          { "subject": "Construction Engineering", "credit": 3 },
          { "subject": "Surveying", "credit": 2 },
          { "subject": "Surveying Practice", "credit": 1 },
          { "subject": "Reinforced Concrete Structures 2", "credit": 3 },
          { "subject": "Foundation Engineering", "credit": 3 },
          { "subject": "RC Design Project", "credit": 1 },
          { "subject": "Steel Structure Design Project", "credit": 1 },
          { "subject": "Civil Engineering Elective 1", "credit": 3 }
        ],
        "Summer Semester 3": [
          { "subject": "Internship", "credit": 3 }
        ],
        "Semester 7": [
          { "subject": "Construction Management", "credit": 3 },
          { "subject": "Foundation Design Project", "credit": 1 },
          { "subject": "Construction Engineering Project", "credit": 1 },
          { "subject": "Professional Ethics and Working Skills", "credit": 3 },
          { "subject": "Civil Engineering Elective 2", "credit": 3 },
          { "subject": "Civil Engineering Elective 3", "credit": 3 },
          { "subject": "Supporting Elective 1", "credit": 3 }
        ],
        "Semester 8": [
          { "subject": "Thesis / Graduation Project", "credit": 10 },
          { "subject": "Supporting Elective 2", "credit": 3 }
        ]
    },
    "Bachelor of Engineering in Construction Management":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Engineering Mechanics and Mechanics of Materials", "credit": 3 },
        { "subject": "Computer-Aided Design and Drafting", "credit": 3 },
        { "subject": "Computer-Aided Design and Drafting Practice", "credit": 1 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Introduction to Construction Management", "credit": 2 },
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Structural Analysis 1", "credit": 2 },
        { "subject": "Construction Materials", "credit": 3 },
        { "subject": "Physical Training 1", "credit": 0 }
      ],
      "Summer Semester 1": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Steel Structures", "credit": 3 },
        { "subject": "Reinforced Concrete 1", "credit": 3 },
        { "subject": "Operation Management in Construction", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Construction Management Project", "credit": 1 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 },
        { "subject": "Scientific Socialism", "credit": 2 }
      ],
      "Semester 4": [
        { "subject": "Soil Mechanics and Foundation", "credit": 3 },
        { "subject": "Construction Economics", "credit": 3 },
        { "subject": "Ho Chi Minh’s Thoughts", "credit": 2 },
        { "subject": "General Law", "credit": 3 },
        { "subject": "Construction Measurement and Cost Estimating", "credit": 3 },
        { "subject": "Engineering Ethics and Critical Thinking", "credit": 3 }
      ],
      "Summer Semester 2": [
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Building Information Modelling", "credit": 3 },
        { "subject": "Construction Planning and Scheduling", "credit": 3 },
        { "subject": "Construction Measurement and Cost Estimating Project", "credit": 1 },
        { "subject": "Construction Cost Management", "credit": 3 },
        { "subject": "Construction Procurement and Tendering", "credit": 3 },
        { "subject": "Artificial Intelligence in Civil Engineering and Construction Management", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Construction Planning and Scheduling Project", "credit": 1 },
        { "subject": "Surveying", "credit": 2 },
        { "subject": "Statistics for Business", "credit": 3 },
        { "subject": "Project Feasibility Study and Appraisal", "credit": 3 },
        { "subject": "Building Information Management Project", "credit": 1 },
        { "subject": "Human Resource Management", "credit": 3 },
        { "subject": "Principles of Marketing", "credit": 3 }
      ],
      "Summer Semester 3": [
        { "subject": "Internship", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Business Research Methods", "credit": 3 },
        { "subject": "Construction Project Management (PMBOK extension)", "credit": 3 },
        { "subject": "CM Elective 1 (list A)", "credit": 3 },
        { "subject": "CM Elective 2 (list A)", "credit": 3 },
        { "subject": "CM Elective 3 (list A)", "credit": 3 },
        { "subject": "CM Elective 4 (list B)", "credit": 1 }
      ],
      "Semester 8": [
        { "subject": "Risk Management", "credit": 3 },
        { "subject": "Quantitative Method for Business", "credit": 3 },
        { "subject": "IU Elective 1 (list C)", "credit": 3 },
        { "subject": "IU Elective 2 (list C)", "credit": 3 },
        { "subject": "Construction Jobsite Management", "credit": 3 },
        { "subject": "Contract Management – FIDIC contracts", "credit": 3 },
        { "subject": "Value Engineering", "credit": 3 },
        { "subject": "Construction Engineering", "credit": 3 }
      ],
      "Semester 9": [
        { "subject": "Leadership", "credit": 3 },
        { "subject": "Graduation Thesis", "credit": 10 }
      ]
    },
    "Deakin University":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Engineering Mechanics - Statics", "credit": 3 },
        { "subject": "Introduction to Civil Engineering", "credit": 1 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Engineering Ethics and Professional Skills", "credit": 3 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Introduction to Computing for Civil Engineers", "credit": 3 },
        { "subject": "Physics 2", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Computer-Aided Design and Drafting (CADD)", "credit": 3 },
        { "subject": "Practice CADD", "credit": 1 },
        { "subject": "Mechanics of Materials 1", "credit": 2 },
        { "subject": "Mechanics of Materials Laboratory", "credit": 1 },
        { "subject": "Fluid Mechanics", "credit": 2 },
        { "subject": "Fluid Mechanics Lab", "credit": 1 },
        { "subject": "Computational Methods for Civil Engineering", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Structural Analysis 1", "credit": 2 },
        { "subject": "Mechanics of Materials 2", "credit": 2 },
        { "subject": "Construction Materials", "credit": 3 },
        { "subject": "Soil Mechanics", "credit": 3 },
        { "subject": "Soil Mechanics Lab", "credit": 1 },
        { "subject": "Civil Architecture", "credit": 2 },
        { "subject": "Probability and Statistics", "credit": 3 }
      ],
      "Trimester 1 (Deakin)": [
        { "subject": "Water Engineering Design", "credit": 2 },
        { "subject": "Hydrology and Hydraulics", "credit": 1 },
        { "subject": "Theory of Structures", "credit": 1 }
      ],
      "Trimester 2 (Deakin)": [
        { "subject": "Reinforced Concrete and Steel Structures", "credit": 2 },
        { "subject": "Geotechnical Engineering", "credit": 1 },
        { "subject": "Professional Practice", "credit": 1 }
      ],
      "Trimester 3 (Deakin)": [
        { "subject": "Engineering Project A", "credit": 2 },
        { "subject": "Traffic and Transport Engineering", "credit": 1 },
        { "subject": "Elective (Level 3, 4, or 7)", "credit": 1 }
      ],
      "Trimester 4 (Deakin)": [
        { "subject": "Engineering Project B", "credit": 2 },
        { "subject": "Infrastructure Engineering", "credit": 1 },
        { "subject": "Elective", "credit": 1 }
      ]
    }
  }, 
  "School of Electrical Engineering": {
    "Bachelor of Electronics and Telecommunications Engineering":{
      "Semester 1": [
        {"subject": "Calculus 1", "credit": 4},
        {"subject": "Physics 1 (Mechanics)", "credit": 2},
        {"subject": "Chemistry for Engineers", "credit": 3},
        {"subject": "Chemistry Laboratory", "credit": 1},
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Intro to Computer for Engineers", "credit": 3},
        {"subject": "Physical Training 1", "credit": 0}
      ],
      "Semester 2": [
        {"subject": "Calculus 2", "credit": 4},
        {"subject": "Applied Linear Algebra", "credit": 2},
        {"subject": "Physics 2 (Thermodynamics)", "credit": 2},
        {"subject": "General Laws", "credit": 3},
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Introduction to EE", "credit": 3},
        {"subject": "Physical Training 2", "credit": 0}  
      ],
      "Semester 3": [        
        {"subject": "Calculus 3", "credit": 4},
        {"subject": "Physics 3 (Electricity & Magnetism)", "credit": 3},
        {"subject": "Physics 3 Lab", "credit": 1},
        {"subject": "Principles of EE 1", "credit": 3},
        {"subject": "Principles of EE 1 Lab", "credit": 1},
        {"subject": "Programming for Engineers", "credit": 2},
        {"subject": "Programming for Engineers Lab", "credit": 1},
        {"subject": "Philosophy of Marxism and Leninism", "credit": 3}
      ],
      "Semester 4": [
        {"subject": "Differential Equations", "credit": 4},
        {"subject": "Probability & Random Process", "credit": 3},
        {"subject": "Principles of EE 2", "credit": 3},
        {"subject": "Principles of EE 2 Lab", "credit": 1},
        {"subject": "Digital Logic Design", "credit": 3},
        {"subject": "Digital Logic Design Lab", "credit": 1},
        {"subject": "Political economics of Marxism and Leninism", "credit": 2}
      ],
      "Semester 5": [
        {"subject": "Signals & Systems", "credit": 3},
        {"subject": "Signals & Systems Lab", "credit": 1},
        {"subject": "Micro-processing Systems", "credit": 3},
        {"subject": "Micro-processing Systems Lab", "credit": 1},
        {"subject": "Electromagnetic Theory", "credit": 3},
        {"subject": "Scientific Socialism", "credit": 2},
        {"subject": "Electronics Devices", "credit": 3},
        {"subject": "Electronics Devices Lab", "credit": 1}
      ],
      "Semester 6": [
        {"subject": "Digital Signal Processing", "credit": 3},
        {"subject": "Digital Signal Processing Lab", "credit": 1},
        {"subject": "Principles of Communication Systems", "credit": 3},
        {"subject": "Principles of Communication Systems Lab", "credit": 1},
        {"subject": "Capstone Design 1", "credit": 2},
        {"subject": "Physics 4 (Optics & Atomics)", "credit": 2},
        {"subject": "Engineering Ethics and Critical Thinking", "credit": 3},
        {"subject": "History of Vietnamese Communist Party", "credit": 2}
      ],
      "Summer Semester": [
        {"subject": "Military Training", "credit": 0},
        {"subject": "Summer Internship", "credit": 0}
      ],
      "Semester 7": [
        {"subject": "Capstone Design 2", "credit": 2},
        {"subject": "Power Electronics", "credit": 3},
        {"subject": "Power Electronics Lab", "credit": 1},
        {"subject": "General Elective", "credit": 3},
        {"subject": "Ho Chi Minh's Thoughts", "credit": 2},
        {"subject": "EE Elective Course 01", "credit": 3},
        {"subject": "EE Elective Course 02", "credit": 3}
      ],
      "Semester 8": [
        {"subject": "Senior Project", "credit": 2},
        {"subject": "EE Elective Course 03", "credit": 4},
        {"subject": "EE Elective Course 04", "credit": 4},
        {"subject": "EE Elective Course 05", "credit": 4},
        {"subject": "Entrepreneurship", "credit": 3}
      ],
      "Semester 9": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Bachelor of Control Engineering and Automation":{
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1 (Mechanics)", "credit": 2 },
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 2": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Physics 2 (Thermodynamics)", "credit": 2 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Introduction to EE", "credit": 3 },
        { "subject": "Intro to Computer for Engineers", "credit": 3 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 }
      ],
      "Summer Semester 1": [
        { "subject": "History of Vietnamese Communist Party", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Materials Science & Engineering", "credit": 3 },
        { "subject": "Mathematics for Engineers", "credit": 4 },
        { "subject": "Principles of EE 1", "credit": 3 },
        { "subject": "Principles of EE 1 Lab", "credit": 1 },
        { "subject": "Digital Logic Design", "credit": 3 },
        { "subject": "Digital Logic Design Lab", "credit": 1 },
        { "subject": "Programming for Engineers", "credit": 3 },
        { "subject": "Programming for Engineers Lab", "credit": 1 }
      ],
      "Semester 4": [
        { "subject": "Probability & Random Process", "credit": 3 },
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Physics 4 (Optics & Atomics)", "credit": 2 },
        { "subject": "Electromagnetic Theory", "credit": 3 },
        { "subject": "Principles of EE 2", "credit": 3 },
        { "subject": "Principles of EE 2 Lab", "credit": 1 },
        { "subject": "Electronics Devices", "credit": 3 },
        { "subject": "Electronics Devices Lab", "credit": 1 }
      ],
      "Summer Semester 2": [
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Signals & Systems", "credit": 3 },
        { "subject": "Signals & Systems Lab", "credit": 1 },
        { "subject": "Micro-processing Systems", "credit": 3 },
        { "subject": "Micro-processing Systems Lab", "credit": 1 },
        { "subject": "Theory of Automatic Control", "credit": 4 },
        { "subject": "Capstone Design 1", "credit": 2 },
        { "subject": "Engineering Ethics and Professional Skills", "credit": 3 },
        { "subject": "Ho Chi Minh's Thoughts", "credit": 2 },
        { "subject": "General Elective", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Digital Signal Processing", "credit": 3 },
        { "subject": "Digital Signal Processing Lab", "credit": 1 },
        { "subject": "PC Based Control and SCADA System", "credit": 3 },
        { "subject": "PC Based Control and SCADA System Lab", "credit": 1 },
        { "subject": "Programmable Logic Control", "credit": 3 },
        { "subject": "Programmable Logic Control Lab", "credit": 1 },
        { "subject": "Sensors and Instrumentation", "credit": 3 },
        { "subject": "Capstone Design 2", "credit": 2 },
        { "subject": "AC Elective Course 01", "credit": 4 }
      ],
      "Summer Semester 3": [
        { "subject": "Summer Internship", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Senior Project", "credit": 2 },
        { "subject": "AC Elective Course 02", "credit": 3 },
        { "subject": "AC Elective Course 03", "credit": 3 },
        { "subject": "AC Elective Course 04", "credit": 3 },
        { "subject": "Entrepreneurship", "credit": 3 },
        { "subject": "AC Elective Course 05", "credit": 3 }
      ],
  "Semester 8": [
    { "subject": "Thesis", "credit": 10 }
  ]
    },
    "University of Nottingham (2+2)" :{
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1 (Mechanics)", "credit": 2 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Introduction to EE", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Physics 2 (Thermodynamics)", "credit": 2 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Intro to Computer for Engineers", "credit": 3 }
       ],
      "Semester 3": [
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Physics 3", "credit": 3 },
        { "subject": "Physics 3 Laboratory", "credit": 1 },
        { "subject": "Principles of EE 1", "credit": 3 },
        { "subject": "Principles of EE 1 Lab", "credit": 1 },
        { "subject": "Digital Logic Design", "credit": 3 },
        { "subject": "Digital Logic Design Lab", "credit": 1 },
        { "subject": "Programming for Engineers (C)", "credit": 3 },
        { "subject": "Programming for Engineers Lab", "credit": 1 }
      ],
      "Semester 4": [
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Probability & Random Process", "credit": 3 },
        { "subject": "Physics 4", "credit": 2 },
        { "subject": "Electromagnetic Theory", "credit": 3 },
        { "subject": "Principles of EE 2", "credit": 3 },
        { "subject": "Principles of EE 2 Laboratory", "credit": 1 },
        { "subject": "General Electives", "credit": 3 }
      ]
    },
    "University of West of England" :{
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1 (Mechanics)", "credit": 2 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Introduction to EE", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Physics 2 (Thermodynamics)", "credit": 2 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Intro to Computer for Engineers", "credit": 3 }
      ],
      "Semester 3": [
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Physics 3", "credit": 3 },
        { "subject": "Physics 3 Laboratory", "credit": 1 },
        { "subject": "Principles of EE 1", "credit": 3 },
        { "subject": "Principles of EE 1 Lab", "credit": 1 },
        { "subject": "Digital Logic Design", "credit": 3 },
        { "subject": "Digital Logic Design Lab", "credit": 1 },
        { "subject": "Programming for Engineers (C)", "credit": 3 },
        { "subject": "Programming for Engineers Lab", "credit": 1 }
      ],
      "Semester 4": [
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Probability & Random Process", "credit": 3 },
        { "subject": "Physics 4", "credit": 2 },
        { "subject": "Electromagnetic Theory", "credit": 3 },
        { "subject": "Principles of EE 2", "credit": 3 },
        { "subject": "Principles of EE 2 Laboratory", "credit": 1 },
        { "subject": "General Electives", "credit": 3 }
      ]
    },
    "SUNY Binghamton, USA" :{
      "Semester 1": [
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1 (Mechanics)", "credit": 2 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Introduction to EE", "credit": 3 },
        { "subject": "Physical Training 1", "credit": 0 }
      ],
      "Semester 2": [
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Physics 2 (Thermodynamics)", "credit": 2 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Intro to Computer for Engineers", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 }
      ],
      "Semester 3": [
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Physics 3", "credit": 3 },
        { "subject": "Physics 3 Laboratory", "credit": 1 },
        { "subject": "Principles of EE 1", "credit": 3 },
        { "subject": "Principles of EE 1 Lab", "credit": 1 },
        { "subject": "Digital Logic Design", "credit": 3 },
        { "subject": "Digital Logic Design Laboratory", "credit": 1 },
        { "subject": "Programming for Engineers (C)", "credit": 3 },
        { "subject": "Programming for Engineers Lab", "credit": 1 }
      ],
      "Semester 4": [
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Probability & Random Process", "credit": 3 },
        { "subject": "Physics 4", "credit": 2 },
        { "subject": "Principles of EE 2", "credit": 3 },
        { "subject": "Principles of EE 2 Laboratory", "credit": 1 },
        { "subject": "Microprocessor Systems", "credit": 3 },
        { "subject": "Microprocessor Systems Lab", "credit": 1 }
      ]
    }
  }, 
  "Physics and Space Engineering": {
    "Space Engineering Program (Big Data Analytics and Applications)": {
      "Semester 1": [
        { "subject": "Academic English 1", "credit": 4 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "General Physics 1", "credit": 4 },
        { "subject": "General Physics 1 Laboratory", "credit": 1 },
        { "subject": "Introduction to Computer for Engineers", "credit": 2 },
        { "subject": "Physical Training", "credit": 0 }
      ],
      "Semester 2": [
        { "subject": "Academic English 2", "credit": 4 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "General Physics 2", "credit": 4 },
        { "subject": "General Physics 2 Laboratory", "credit": 1 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 }
      ],
      "Semester 3": [
        { "subject": "Introduction to Space Engineering", "credit": 2 },
        { "subject": "General Physics 3", "credit": 2 },
        { "subject": "General Physics 3 Laboratory", "credit": 1 },
        { "subject": "Mathematics for Engineers", "credit": 4 },
        { "subject": "Programming for Engineers", "credit": 3 },
        { "subject": "Programming for Engineers Laboratory", "credit": 1 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 4": [
        { "subject": "Differential Equations", "credit": 2 },
        { "subject": "Probability and Statistics for Engineers", "credit": 3 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "Introduction to Relativity and Modern Physics", "credit": 3 },
        { "subject": "Optics and Photonics", "credit": 2 },
        { "subject": "Earth Observation and the Environment", "credit": 3 }
      ],
      "Semester 5": [
        { "subject": "Introduction to Signals and Systems", "credit": 3 },
        { "subject": "Signals and Systems Laboratory", "credit": 1 },
        { "subject": "Satellite Technology", "credit": 3 },
        { "subject": "Space Environment", "credit": 3 },
        { "subject": "iOS Programming Fundamentals", "credit": 4 },
        { "subject": "History of Vietnamese Communist Party", "credit": 2 }
      ],
      "Semester 6": [
        { "subject": "Geolocation App Development for iOS", "credit": 4 },
        { "subject": "Navigation Systems", "credit": 3 },
        { "subject": "Introduction to Space Communications", "credit": 3 },
        { "subject": "Introduction to Digital Image Processing", "credit": 2 },
        { "subject": "Digital Image Processing Laboratory", "credit": 1 },
        { "subject": "Engineering Ethics and Professional Skills", "credit": 3 }
      ],
      "Summer Semester": [
        { "subject": "Military Training", "credit": 0 },
        { "subject": "Internship", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Digital Signal Processing", "credit": 3 },
        { "subject": "Digital Signal Processing Laboratory", "credit": 1 },
        { "subject": "Project Management", "credit": 3 },
        { "subject": "Remote Sensing", "credit": 3 },
        { "subject": "Big Data Analytics for Remote Sensing", "credit": 3 },
        { "subject": "Big Data Analytics for Remote Sensing Laboratory", "credit": 1 }
      ],
      "Semester 8": [
        { "subject": "Thesis", "credit": 10 }
      ]
    }
  }, 
  "Industrial Engineering and Logistics Systems": {
    "Intelligent Industrial Systems":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Chemistry for Engineers", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Introduction to Industrial Engineering", "credit": 1 },
        { "subject": "Engineering Drawing", "credit": 2 },
        { "subject": "Physics 3", "credit": 3 }
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Production Management", "credit": 3 },
        { "subject": "Introduction to Computing", "credit": 3 },
        { "subject": "Engineering Probability & Statistics", "credit": 4 },
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "General Law", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Engineering Economy", "credit": 3 },
        { "subject": "Deterministic Models in OR", "credit": 3 },
        { "subject": "Work Design & Ergonomics", "credit": 4 },
        { "subject": "Project Management", "credit": 3 },
        { "subject": "Product Design & Development", "credit": 3 },
        { "subject": "History of the Communist Party of Vietnam", "credit": 2 },
        { "subject": "HCM's Thoughts", "credit": 2 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Internship 1", "credit": 2 },
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Management Information System with ERP Applications", "credit": 3 },
        { "subject": "Quality Management", "credit": 3 },
        { "subject": "CAD/CAM/CNC", "credit": 3 },
        { "subject": "Data Collection, Analysis, and Applications", "credit": 3 },
        { "subject": "Inventory Management", "credit": 3 },
        { "subject": "Time Series & Forecasting Techniques", "credit": 2 },
        { "subject": "ISE Elective Course Group 1", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Scientific Writing", "credit": 2 },
        { "subject": "Simulation Models in IE", "credit": 4 },
        { "subject": "Scheduling & Sequencing", "credit": 3 },
        { "subject": "Lean Production", "credit": 3 },
        { "subject": "Experimental Design", "credit": 3 },
        { "subject": "Probabilistic Models in OR", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 2", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Capstone 1", "credit": 3 },
        { "subject": "Multi-Criteria Decision Making", "credit": 3 },
        { "subject": "Facility Layout", "credit": 3 },
        { "subject": "ISE Elective Course Group 2", "credit": 6 }, 
        { "subject": "Free Elective Course Group 3", "credit": 3 } 
      ],
      "Semester 8": [
        { "subject": "Thesis", "credit": 10 }
      ]
    },
    "Industrial Analytics":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Chemistry for Engineers", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Introduction to Industrial Engineering", "credit": 1 },
        { "subject": "Engineering Drawing", "credit": 2 },
        { "subject": "Physics 3", "credit": 3 }
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Production Management", "credit": 3 },
        { "subject": "Introduction to Computing", "credit": 3 },
        { "subject": "Engineering Probability & Statistics", "credit": 4 },
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "General Law", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Engineering Economy", "credit": 3 },
        { "subject": "Deterministic Models in OR", "credit": 3 },
        { "subject": "Work Design & Ergonomics", "credit": 4 },
        { "subject": "Project Management", "credit": 3 },
        { "subject": "Product Design & Development", "credit": 3 },
        { "subject": "History of the Communist Party of Vietnam", "credit": 2 },
        { "subject": "HCM's Thoughts", "credit": 2 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Internship 1", "credit": 2 },
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Management Information System with ERP Applications", "credit": 3 },
        { "subject": "Quality Management", "credit": 3 },
        { "subject": "CAD/CAM/CNC", "credit": 3 },
        { "subject": "Inventory Management", "credit": 3 },
        { "subject": "Time Series & Forecasting Techniques", "credit": 2 },
        { "subject": "Data Collection, Analysis, and Applications", "credit": 3 },
        { "subject": "ISE Elective Course Group 1", "credit": 3 } 
      ],
      "Semester 6": [
        { "subject": "Scientific Writing", "credit": 2 },
        { "subject": "Simulation Models", "credit": 4 },
        { "subject": "Scheduling & Sequencing", "credit": 3 },
        { "subject": "Lean Production", "credit": 3 },
        { "subject": "Predictive Data Analytics and Applications", "credit": 3 },
        { "subject": "Industrial & Commercial Data Systems", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 2", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Capstone 1", "credit": 3 },
        { "subject": "Decision Analytics", "credit": 3 },
        { "subject": "Industrial Process, System Data Analysis and Modelling", "credit": 3 },
        { "subject": "ISE Elective Course Group 2", "credit": 6 }, 
        { "subject": "Free Elective Course Group 3", "credit": 3 } 
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Logistics and Supply Chain Management Engineer":{
    "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Chemistry for Engineers", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Introduction to Logistics & Supply Chain Management", "credit": 1 },
        { "subject": "Physics 3", "credit": 3 }
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Production Management", "credit": 3 },
        { "subject": "Introduction to Computing", "credit": 3 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Engineering Probability & Statistics", "credit": 4 },
        { "subject": "Principles of Logistics and Supply Chain Management", "credit": 3 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "General Law", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Engineering Economy", "credit": 3 },
        { "subject": "Deterministic Models in OR", "credit": 3 },
        { "subject": "Warehouse Engineering Management", "credit": 3 },
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Import – Export Management", "credit": 3 },
        { "subject": "History of the Communist Party of Vietnam", "credit": 2 },
        { "subject": "HCM’s Thoughts", "credit": 2 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Internship 1", "credit": 2 },
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Materials Handling Systems", "credit": 2 },
        { "subject": "Management Information System with ERP Applications", "credit": 3 },
        { "subject": "Inventory Management", "credit": 3 },
        { "subject": "Procurement Management", "credit": 2 },
        { "subject": "Retail Management", "credit": 3 },
        { "subject": "Time Series & Forecasting Techniques", "credit": 2 },
        { "subject": "LSCM Elective Course Group 1", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Scientific Writing", "credit": 2 },
        { "subject": "Scheduling & Sequencing", "credit": 3 },
        { "subject": "Financial Accounting", "credit": 3 },
        { "subject": "Logistics Engineering & Supply Chain Design", "credit": 3 },
        { "subject": "E-commerce Systems", "credit": 3 },
        { "subject": "Supply Security and Risk Management", "credit": 3 },
        { "subject": "Project Management", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 2", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Capstone 1", "credit": 3 },
        { "subject": "Decision Analytics", "credit": 3 },
        { "subject": "International Transportation & Logistics", "credit": 3 },
        { "subject": "Supply Chain Modelling and Simulation", "credit": 3 },
        { "subject": "E-Logistics in Supply Chain Management", "credit": 3 },
        { "subject": "LSCM Elective Course Group 2", "credit": 3 }, 
        { "subject": "Free Elective Course Group 3", "credit": 3 } 
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Logistics and Supply Chain Analytics":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Physical Training 1", "credit": 0 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Chemistry for Engineers", "credit": 3 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Introduction to Logistics & Supply Chain Management", "credit": 1 },
        { "subject": "Physics 3", "credit": 3 }
      ],
      "Summer Semester (Year 1)": [
        { "subject": "Philosophy of Marxism and Leninism", "credit": 3 },
        { "subject": "Political Economics of Marxism and Leninism", "credit": 2 }
      ],
      "Semester 3": [
        { "subject": "Production Management", "credit": 3 },
        { "subject": "Introduction to Computing", "credit": 3 },
        { "subject": "Applied Linear Algebra", "credit": 2 },
        { "subject": "Engineering Probability & Statistics", "credit": 4 },
        { "subject": "Principles of Logistics and Supply Chain Management", "credit": 3 },
        { "subject": "Scientific Socialism", "credit": 2 },
        { "subject": "General Law", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Engineering Economy", "credit": 3 },
        { "subject": "Deterministic Models in OR", "credit": 3 },
        { "subject": "Warehouse Engineering Management", "credit": 3 },
        { "subject": "Calculus 3", "credit": 4 },
        { "subject": "Import - Export Management", "credit": 3 },
        { "subject": "History of the Communist Party of Vietnam", "credit": 2 },
        { "subject": "HCM's Thoughts", "credit": 2 }
      ],
      "Summer Semester (Year 2)": [
        { "subject": "Internship 1", "credit": 2 },
        { "subject": "Military Training", "credit": 0 }
      ],
      "Semester 5": [
        { "subject": "Data Collection, Analysis, and Applications", "credit": 3 },
        { "subject": "Materials Handling Systems", "credit": 2 },
        { "subject": "Management Information System with ERP Applications", "credit": 3 },
        { "subject": "Inventory Management", "credit": 3 },
        { "subject": "Procurement Management", "credit": 2 },
        { "subject": "Retail Management", "credit": 3 },
        { "subject": "Time Series & Forecasting Techniques", "credit": 2 },
        { "subject": "LSCM Elective Course Group 1", "credit": 3 } 
      ],
      "Semester 6": [
        { "subject": "Scientific Writing", "credit": 2 },
        { "subject": "Scheduling & Sequencing", "credit": 3 },
        { "subject": "Financial Accounting", "credit": 3 },
        { "subject": "Predictive Data Analytics and Applications", "credit": 3 },
        { "subject": "Logistics Engineering & Supply Chain Design", "credit": 3 },
        { "subject": "Supply Security and Risk Management", "credit": 3 },
        { "subject": "Project Management", "credit": 3 }
      ],
      "Summer Semester (Year 3)": [
        { "subject": "Internship 2", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Capstone 1", "credit": 3 },
        { "subject": "Decision Analytics", "credit": 3 },
        { "subject": "International Transportation & Logistics", "credit": 3 },
        { "subject": "Data Mining in Supply Chain", "credit": 3 },
        { "subject": "LSCM Elective Course Group 2", "credit": 3 },
        { "subject": "Free Elective Course Group 3", "credit": 3 } 
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Binghamton University - Industrial and Systems Engineering":{
      "Semester 1": [
        { "subject": "Writing AE1", "credit": 2 },
        { "subject": "Listening AE1", "credit": 2 },
        { "subject": "Calculus 1", "credit": 4 },
        { "subject": "Physics 1", "credit": 2 },
        { "subject": "Chemistry for Engineers", "credit": 3 },
        { "subject": "Chemistry Laboratory", "credit": 1 },
        { "subject": "Physical Training 1", "credit": 0 }
      ],
      "Semester 2": [
        { "subject": "Writing AE2", "credit": 2 },
        { "subject": "Speaking AE2", "credit": 2 },
        { "subject": "Calculus 2", "credit": 4 },
        { "subject": "Physics 2", "credit": 2 },
        { "subject": "Physical Training 2", "credit": 0 },
        { "subject": "Introduction to Industrial Engineering", "credit": 1 }
      ],
      "Semester 3": [
        { "subject": "Differential Equations or Calculus 3", "credit": 4 },
        { "subject": "Physics 3", "credit": 3 },
        { "subject": "Physics 3 Lab", "credit": 1 },
        { "subject": "Critical Thinking", "credit": 3 },
        { "subject": "Engineering Probability", "credit": 4 }
      ],
      "Semester 4": [
        { "subject": "Human Factors", "credit": 4 },
        { "subject": "Engineering Economy", "credit": 3 },
        { "subject": "Physics 4", "credit": 2 }
      ]
    }
  }, 
  "Mathematics": {
    "Bachelor of Science in Statistics":{
      "Semester 1": [
        { "subject": "Analysis 1", "credit": 3 },
        { "subject": "General Law", "credit": 3 },
        { "subject": "Introduction to Python", "credit": 4 },
        { "subject": "Writing AE1", "credit": 2},
        { "subject": "Listening AE1", "credit": 2}
      ],
      "Semester 2": [
        { "subject": "Analysis 2", "credit": 4 },
        { "subject": "Linear Algebra", "credit": 4 },
        { "subject": "Object-Oriented Programming", "credit": 4 },
        { "subject": "Financial Accounting", "credit": 4 },
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2}
      ],
      "Semester 3": [
        { "subject": "Real Analysis", "credit": 4 },
        { "subject": "Analysis 3", "credit": 4 },
        { "subject": "Probability", "credit": 3 },
        { "subject": "Database Management System", "credit": 4 },
        { "subject": "Introduction to Statistics", "credit": 4 }
      ],
      "Semester 4": [
        { "subject": "Statistics", "credit": 3 },
        { "subject": "Introduction to Machine Learning", "credit": 4 },
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Introduction to Business Administration", "credit": 4 }
      ],
      "Semester 5": [
        { "subject": "Stochastic Modeling", "credit": 4 },
        { "subject": "Numerical Analysis", "credit": 4 },
        { "subject": "Regression Models", "credit": 4 },
        { "subject": "Algorithms and Data Structure", "credit": 4 },
        { "subject": "MAAS Elective #1", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Optimization 1", "credit": 4 },
        { "subject": "Decision Making", "credit": 4 },
        { "subject": "Statistical Computing", "credit": 4 },
        { "subject": "Applied Time Series Analysis", "credit": 4 },
        { "subject": "MAAS Elective #2", "credit": 3 }
      ],
      "Summer Semester": [
        { "subject": "Internship", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Deep Learning", "credit": 4 },
        { "subject": "Bayesian Statistics", "credit": 4 },
        { "subject": "Multivariate Statistical Analysis", "credit": 4 },
        { "subject": "MAAS Elective #3", "credit": 3 },
        { "subject": "MAAS Elective #4", "credit": 3 }
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    },
    "Bachelor of Financial Engineering and Risk Management":{
      "Semester 1": [
        { "subject": "Analysis 1", "credit": 3 },
        { "subject": "Micro Economics", "credit": 4 },
        { "subject": "Introduction to Python", "credit": 4 },
        { "subject": "Writing AE1", "credit": 2},
        { "subject": "Listening AE1", "credit": 2}
      ],
      "Semester 2": [
        { "subject": "Analysis 2", "credit": 3 },
        { "subject": "Linear Algebra", "credit": 4 },
        { "subject": "Financial Economics", "credit": 4 },
        { "subject": "Macro Economics", "credit": 4 },
        { "subject": "Writing AE2", "credit": 2},
        { "subject": "Speaking AE2", "credit": 2}
      ],
      "Semester 3": [
        { "subject": "Real Analysis", "credit": 4 },
        { "subject": "Analysis 3", "credit": 3 },
        { "subject": "Financial Accounting", "credit": 4 },
        { "subject": "Database Management System", "credit": 4 },
        { "subject": "FERM Elective #1", "credit": 3 }
      ],
      "Semester 4": [
        { "subject": "Probability", "credit": 3 },
        { "subject": "Differential Equations", "credit": 4 },
        { "subject": "Introduction to Corporate Finance", "credit": 4 },
        { "subject": "Numerical Analysis", "credit": 4 },
        { "subject": "Financial Management", "credit": 4 }
      ],
      "Semester 5": [
        { "subject": "Statistics", "credit": 3 },
        { "subject": "Random Processes", "credit": 4 },
        { "subject": "Optimization 1", "credit": 4 },
        { "subject": "Software Engineering", "credit": 4 },
        { "subject": "FERM Elective #2", "credit": 3 }
      ],
      "Semester 6": [
        { "subject": "Financial Mathematics 1", "credit": 4 },
        { "subject": "Optimization 2", "credit": 4 },
        { "subject": "Financial Risk Management 1", "credit": 4 },
        { "subject": "Decision Making", "credit": 4 },
        { "subject": "Financial Econometrics", "credit": 4 }
      ],
      "Summer Semester": [
        { "subject": "Internship", "credit": 3 }
      ],
      "Semester 7": [
        { "subject": "Financial Mathematics 2", "credit": 4 },
        { "subject": "Portfolio Management", "credit": 4 },
        { "subject": "Research Methods in Finance", "credit": 4 },
        { "subject": "FERM Elective #3", "credit": 3 },
        { "subject": "FERM Elective #4", "credit": 3 }
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    }
  }, 
  "School of Biomedical Engineering": {
    "Bachelor of Engineering of Biomedical Engineering":{
      "Semester 1": [
        {"subject": "Calculus 1", "credit": 4},
        {"subject": "Physics 1 (Mechanics)", "credit": 2},
        {"subject": "Physics 2 (Thermodynamics)", "credit": 2},
        {"subject": "Writing AE1", "credit": 2},
        {"subject": "Listening AE1", "credit": 2},
        {"subject": "Lab 1A-Biomedical Instrumentations", "credit": 1},
        {"subject": "Triết học Mác-Lênin", "credit": 3},
        {"subject": "Kinh tế chính trị Mác-Lênin", "credit": 2},
        {"subject": "Physical Training 1", "credit": 0}
      ],
      "Semester 2": [
        {"subject": "Calculus 2", "credit": 4},
        {"subject": "Chemistry for Engineers", "credit": 3},
        {"subject": "Chemistry Laboratory", "credit": 1},
        {"subject": "Principles of EE I", "credit": 3},
        {"subject": "Principles of EE I Laboratory", "credit": 1},
        {"subject": "Biology for BME", "credit": 4},
        {"subject": "Writing AE2", "credit": 2},
        {"subject": "Speaking AE2", "credit": 2},
        {"subject": "Lab 1B-Invitro Studies", "credit": 1},
        {"subject": "Physical Training 2", "credit": 0}
      ],
      "Semester 3": [        
        {"subject": "Calculus 3", "credit": 4},
        {"subject": "Chemistry for BME", "credit": 3},
        {"subject": "Chemistry for BME Lab", "credit": 1},
        {"subject": "Introduction to BME", "credit": 4},
        {"subject": "Human Anatomy and Physiology", "credit": 3},
        {"subject": "Design 2A- Electronic Design", "credit": 1},
        {"subject": "Critical Thinking", "credit": 3},
        {"subject": "Lịch sử Đảng Cộng sản Việt Nam", "credit": 2},
        {"subject": "Ho Chi Minh's Thoughts", "credit": 2}
      ],
      "Semester 4": [
        {"subject": "Differential Equations", "credit": 4},
        {"subject": "Applied Informatics + Lab", "credit": 4},
        {"subject": "Engineering Challenges in Medicine I", "credit": 3},
        {"subject": "Biomaterials", "credit": 4},
        {"subject": "Statistics for Health Science", "credit": 3},
        {"subject": "Mechanical design and manufacturing processes in biomedical engineering", "credit": 2},
        {"subject": "Mechanical design and manufacturing processes in biomedical engineering Lab", "credit": 2},
        {"subject": "Design 2B- Medical Instrumentation", "credit": 1}
      ],
      "Semester 5": [
        {"subject": "AI for healthcare", "credit": 3},
        {"subject": "Machine Design", "credit": 3},
        {"subject": "Bioethics", "credit": 3},
        {"subject": "Technical Electives 1", "credit": 4},
        {"subject": "Technical Electives 2", "credit": 4},
        {"subject": "Free Elective 1", "credit": 3},
        {"subject": "Project 1", "credit": 1}
      ],
      "Semester 6": [
        {"subject": "Entrepreneurship in Biomedical Engineering", "credit": 3},
        {"subject": "Technical Electives 3", "credit": 4},
        {"subject": "Technical Electives 4", "credit": 4},
        {"subject": "Technical Electives 5", "credit": 4},
        {"subject": "Project 2", "credit": 1}
      ],
      "Summer Semester": [
        {"subject": "Scientific Socialism", "credit":2},
        {"subject": "Military Training", "credit": 0},
        {"subject": "Internship", "credit": 3}
      ],
      "Semester 7": [
        {"subject": "Free Elective 2", "credit": 3},
        {"subject": "BME Capstone Design + Lab", "credit": 4},
        {"subject": "Pre-thesis", "credit": 1},
        {"subject": "Technical Electives 6", "credit": 3},
        {"subject": "Technical Electives 7", "credit": 3}
      ],
      "Semester 8": [
        {"subject": "Thesis", "credit": 10}
      ]
    }
  } 
}

# Chuyển đổi cấu trúc
output_data = convert_structure(input_data)

# Xuất ra file JSON
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(output_data )