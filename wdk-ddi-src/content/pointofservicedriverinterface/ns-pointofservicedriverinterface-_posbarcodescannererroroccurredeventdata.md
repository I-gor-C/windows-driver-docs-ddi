---
UID: NS:pointofservicedriverinterface._PosBarcodeScannerErrorOccurredEventData
title: "_PosBarcodeScannerErrorOccurredEventData"
author: windows-driver-content
description: This structure contains the error data that is passed to the BarcodeScannerErrorOccurred event.
old-location: pos\posbarcodescannererroroccurredeventdata.htm
old-project: pos
ms.assetid: c9e18ed0-bc34-49ed-a31e-20c82d43860f
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: PosBarcodeScannerErrorOccurredEventData, PosBarcodeScannerErrorOccurredEventData structure, _PosBarcodeScannerErrorOccurredEventData, pointofservicedriverinterface/PosBarcodeScannerErrorOccurredEventData, pos.posbarcodescannererroroccurredeventdata
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pointofservicedriverinterface.h
req.include-header: PointOfServiceDriverInterface.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	PointOfServiceDriverInterface.h
api_name:
-	PosBarcodeScannerErrorOccurredEventData
product:
- Windows
targetos: Windows
req.typenames: PosBarcodeScannerErrorOccurredEventData
---

# _PosBarcodeScannerErrorOccurredEventData structure
This structure contains the error data that is passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757464">BarcodeScannerErrorOccurred</a> event.

## Syntax
```
typedef struct _PosBarcodeScannerErrorOccurredEventData {
  PosEventDataHeader                     Header;
  LONG                                   IsRetriable;
  DriverUnifiedPosErrorSeverity          Severity;
  UINT32                                 VendorErrorCode;
  DriverUnifiedPosErrorReason            Reason;
  UINT32                                 ExtendedReason;
  UINT32                                 MessageLength;
  PosBarcodeScannerDataReceivedEventData PartialData;
} PosBarcodeScannerErrorOccurredEventData;
```

## Members


`Header`

The <a href="https://msdn.microsoft.com/library/windows/hardware/dn772232">PosEventDataHeader</a> structure that describes the amount of memory, in bytes, of the <b>PosBarcodeScannerErrorOccurredEventData</b> structure and trailing error message and scan data.

`IsRetriable`

Indicates whether <a href="http://go.microsoft.com/fwlink/p/?LinkId=314125">ReadFile</a> can be called again to read this event

`Severity`

Contains a value in the <a href="https://msdn.microsoft.com/a8c592fa-2736-49e4-8d4d-8729baef9c49">UnifiedPosErrorSeverity</a> enumeration indicating the severity of the error.

`VendorErrorCode`

Contains a vendor-specific error code.

`Reason`

Contains a value in the <a href="https://msdn.microsoft.com/2bbf5fcf-666e-4265-95cf-7e04670d59da">UnifiedPosErrorReason</a> enumeration indicating the reason for the error.

`ExtendedReason`

Contains additional data about the reason for the error.

`MessageLength`

Indicates the length, in bytes, of the error message.

`PartialData`

If a scanning error occurs, and some scan data was obtained, the partial scan data will be available in this parameter.

## Remarks
The error data should fill the buffer as shown in the following table (in order).

<table>
<tr>
<th>Data</th>
<th>Length in bytes</th>
</tr>
<tr>
<td>
<b>PosBarcodeScannerErrorOccurredEventData</b> structure

</td>
<td>
sizeof(<b>PosBarcodeScannerErrorOccurredEventData</b>)

</td>
</tr>
<tr>
<td>
Error message text

</td>
<td>
<b>MessageLength</b>

</td>
</tr>
<tr>
<td>
Partial scan data

</td>
<td>
<b>PartialData.ScanDataLength</b>

</td>
</tr>
<tr>
<td>
Label data

</td>
<td>
<b>PartialData.ScanDataLabelLength</b>

</td>
</tr>
</table>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include PointOfServiceDriverInterface.h) |