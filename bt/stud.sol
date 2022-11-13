// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.7.0;

contract studentData{
    struct student{
        int rollNo;
        string fName;
        string lName;
        int marks;
    }

    address owner;
    int public stdCount=0;
    mapping(int => student) public stdRecords;
    modifier onlyOwner{
        require(owner==msg.sender);
        _;
    }

    constructor() public{
        owner=msg.sender;
    }

    function addNewRecord(int _rollNo,string memory _fName,string memory _lName,int _marks) public onlyOwner{
        stdCount = stdCount+1;
        stdRecords[stdCount] = student(_rollNo,_fName,_lName,_marks);
    }

    function bonusMarks(int _bonus) public onlyOwner{
        stdRecords[stdCount].marks = stdRecords[stdCount].marks+_bonus;
    }

    fallback() external payable{
        //called whe we call a function which doesn't exist
    }
}
