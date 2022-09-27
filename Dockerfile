FROM python:3.10.7
WORKDIR /mnt/c/Ryu/Kuliah/Semester-5/TST/Teknologi-Sistem-Terintegrasi/
ADD . /mnt/c/Ryu/Kuliah/Semester-5/TST/Teknologi-Sistem-Terintegrasi/
CMD ["python", "test.py"]