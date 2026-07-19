from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.services.ai_service import AIService
from app.config.database import reports_collection


router = APIRouter()

ai_service = AIService()


# Generate AI Medical Report
@router.post("/consultation")
async def consultation(data: dict):

    try:

        print("Incoming Data:")
        print(data)


        report = ai_service.generate_report(
            data
        )


        document = {

            "user_id": data.get("user_id"),
            "age": data.get("age"),
            "height": data.get("height"),
            "weight": data.get("weight"),
            "temperature": data.get("temperature"),
            "symptoms": data.get("symptoms"),
            "description": data.get("description"),
            "medicalHistory": data.get("medicalHistory"),
            "lifestyle": data.get("lifestyle"),
            "ai_report": report
        }


        result = reports_collection.insert_one(
            document
        )


        return {
            "success": True,
            "report_id": str(result.inserted_id),
            "report": report
        }


    except Exception as e:

        print("CONSULTATION ERROR:")
        print(e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Get All Reports (Admin/testing)
@router.get("/reports")
async def get_all_reports():

    try:

        reports = list(
            reports_collection.find()
            .sort("_id", -1)
        )


        for report in reports:

            report["_id"] = str(
                report["_id"]
            )


        return {
            "success": True,
            "reports": reports
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



# Get User Reports
@router.get("/reports/user/{user_id}")
async def get_user_reports(user_id: str):

    try:

        reports = list(
            reports_collection.find(
                {
                    "user_id": user_id
                }
            )
            .sort("_id", -1)
        )


        for report in reports:

            report["_id"] = str(
                report["_id"]
            )


        return {
            "success": True,
            "reports": reports
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



# Get Single Report
@router.get("/reports/{report_id}")
async def get_report(report_id: str):

    try:

        if not ObjectId.is_valid(report_id):

            raise HTTPException(
                status_code=400,
                detail="Invalid report id"
            )


        report = reports_collection.find_one(
            {
                "_id": ObjectId(report_id)
            }
        )


        if not report:

            raise HTTPException(
                status_code=404,
                detail="Report not found"
            )


        report["_id"] = str(
            report["_id"]
        )


        return {
            "success": True,
            "report": report
        }


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )