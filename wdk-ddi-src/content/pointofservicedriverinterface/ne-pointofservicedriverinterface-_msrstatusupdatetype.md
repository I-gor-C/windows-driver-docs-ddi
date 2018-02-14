---
UID: NE:pointofservicedriverinterface._MsrStatusUpdateType
title: "_MsrStatusUpdateType"
author: windows-driver-content
description: This enumeration defines the constants that indicate the magnetic stripe reader (MSR) status.
old-location: pos\msrstatusupdatetype.htm
old-project: pos
ms.assetid: f7e055ac-df7c-4993-b7aa-f455c4548d5e
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: pointofservicedriverinterface/MsrStatusUpdateType_Extended, MsrStatusUpdateType_Off, MsrStatusUpdateType_Offline, pointofservicedriverinterface/MsrStatusUpdateType_Unauthenticated, MsrStatusUpdateType_Extended, pointofservicedriverinterface/MsrStatusUpdateType_Online, MsrStatusUpdateType_Online, pointofservicedriverinterface/MsrStatusUpdateType_Off, pointofservicedriverinterface/MsrStatusUpdateType_Offline, MsrStatusUpdateType_Unauthenticated, MsrStatusUpdateType_Authenticated, _MsrStatusUpdateType, pos.msrstatusupdatetype, MsrStatusUpdateType, MsrStatusUpdateType enumeration, pointofservicedriverinterface/MsrStatusUpdateType, MsrStatusUpdateType_OffOrOffline, pointofservicedriverinterface/MsrStatusUpdateType_Authenticated, pointofservicedriverinterface/MsrStatusUpdateType_OffOrOffline
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicedriverinterface.h
req.include-header: Pointofservicedriverinterface.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicedriverinterface.h
apiname:
-	MsrStatusUpdateType
product: Windows
targetos: Windows
req.typenames: MsrStatusUpdateType
---

# _MsrStatusUpdateType Enumeration
This enumeration defines the constants that indicate the magnetic stripe reader (MSR) status.

## Syntax
````
typedef enum _MsrStatusUpdateType { 
  MsrStatusUpdateType_Online           = 0,
  MsrStatusUpdateType_Off,
  MsrStatusUpdateType_Offline,
  MsrStatusUpdateType_OffOrOffline,
  MsrStatusUpdateType_Unauthenticated,
  MsrStatusUpdateType_Authenticated,
  MsrStatusUpdateType_Extended
} MsrStatusUpdateType;
````

## Constants

<table>
            
                <tr>
                    <td>MsrStatusUpdateType_Authenticated</td>
                    <td>The device is authenticated. This is valid if the device supports authentication.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_Extended</td>
                    <td>Vendor-specific status information. Reported in IMagneticStripeReaderStatusUpdatedEventArgs.ExtendedStatus.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_Off</td>
                    <td>The device is powered off or is detached from the terminal. This is valid if <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-driverunifiedpospowerreportingtype.md">UnifiedPosPowerReportingType</a> is <b>Advanced</b>.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_Offline</td>
                    <td>The device is powered on but is not ready, or is unable, to respond to requests. This is valid if <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-driverunifiedpospowerreportingtype.md">UnifiedPosPowerReportingType</a> is <b>Advanced</b>.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_OffOrOffline</td>
                    <td>The device is either off or offline. This is valid if <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-driverunifiedpospowerreportingtype.md">UnifiedPosPowerReportingType</a> is <b>Standard</b>.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_Online</td>
                    <td>The device is powered on. This is valid if <a href="..\pointofservicecommontypes\ne-pointofservicecommontypes-driverunifiedpospowerreportingtype.md">UnifiedPosPowerReportingType</a> is <b>Standard</b> or <b>Advanced</b>.</td>
                </tr>
            
                <tr>
                    <td>MsrStatusUpdateType_Unauthenticated</td>
                    <td>The device is not authenticated. This is valid if the device supports authentication.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |