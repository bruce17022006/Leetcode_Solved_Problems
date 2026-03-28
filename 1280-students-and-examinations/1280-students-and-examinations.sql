SELECT 
    s.student_id, 
    s.student_name, 
    s2.subject_name, 
    COUNT(s1.student_id) AS attended_exams
FROM Students s 
CROSS JOIN Subjects s2 
LEFT JOIN Examinations s1 
    ON s.student_id = s1.student_id 
    AND s2.subject_name = s1.subject_name 
GROUP BY s.student_id, s.student_name, s2.subject_name 
ORDER BY s.student_id, s2.subject_name;
