---
UID: NE:pointofservicecommontypes._PosDeviceType
title: "_PosDeviceType"
author: windows-driver-content
description: This enumeration defines values used in the PosDeviceBasicsType structure to indicate the type of device (for instance, barcode scanner or magnetic stripe reader).
old-location: pos\posdevicetype.htm
old-project: pos
ms.assetid: 1e0b4b66-f9aa-4315-a07d-b6fd47f10371
ms.author: windowsdriverdev
ms.date: 2/19/2018
ms.keywords: pointofservicecommontypes/PosDeviceType_MagneticStripeReader, PosDeviceType enumeration, PosDeviceType, pos.posdevicetype, PosDeviceType_Printer, pointofservicecommontypes/PosDeviceType_Printer, pointofservicecommontypes/PosDeviceType, pointofservicecommontypes/PosDeviceType_CashDrawer, pointofservicecommontypes/PosDeviceType_Max, PosDeviceType_CashDrawer, PosDeviceType_MagneticStripeReader, pointofservicecommontypes/PosDeviceType_Unknown, PosDeviceType_BarcodeScanner, PosDeviceType_Unknown, pointofservicecommontypes/PosDeviceType_BarcodeScanner, _PosDeviceType, PosDeviceType_Max
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicecommontypes.h
req.include-header: Pointofservicecommontypes.h
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
req.irql: Called at PASSIVE_LEVEL.
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicecommontypes.h
apiname:
-	PosDeviceType
product: Windows
targetos: Windows
req.typenames: PosDeviceType
---

# _PosDeviceType Enumeration
This enumeration defines values used in the <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_posdevicebasicstype.md">PosDeviceBasicsType</a> structure to indicate the type of device (for instance, barcode scanner or magnetic stripe reader).

## Syntax
````
typedef enum _PosDeviceType { 
  PosDeviceType_Unknown               = 0,
  PosDeviceType_BarcodeScanner        = 1,
  PosDeviceType_MagneticStripeReader  = 2,
  PosDeviceType_Printer               = 3,
  PosDeviceType_CashDrawer            = 4,
  PosDeviceType_Max                   = 5
} PosDeviceType;
````

## Constants

<table>
            
                <tr>
                    <td>PosDeviceType_BarcodeScanner</td>
                    <td>Indicates that the type of device is a barcode scanner.</td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_CashDrawer</td>
                    <td>Indicates that the type of device is a cash drawer.</td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_LineDisplay</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_MagneticStripeReader</td>
                    <td>Indicates that the type of device is a magnetic stripe reader.</td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_Max</td>
                    <td>Unused.</td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_Printer</td>
                    <td>Indicates that the type of device is a printer.</td>
                </tr>
            
                <tr>
                    <td>PosDeviceType_Unknown</td>
                    <td>Indicates that the type of device is not known.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicecommontypes.h (include Pointofservicecommontypes.h) |