---
UID: NE:pointofservicedriverinterface._MsrStatisticsEntryType
title: "_MsrStatisticsEntryType"
author: windows-driver-content
description: This enumeration defines the kinds of magnetic stripe reader statistics.
old-location: pos\mststatisticsentrytype.htm
old-project: pos
ms.assetid: b3c9fac6-79b3-4a81-92af-004eb17a22f5
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: MsrStatisticsEntryType_ChallengeRequestCount, MsrStatisticsEntryType_CommunicationErrorCount, MsrStatisticsEntryType_Count, MsrStatisticsEntryType_FailedCardAuthenticationDataCount, MsrStatisticsEntryType_FailedDeviceAuthenticationCount, MsrStatisticsEntryType_FailedReadCount, MsrStatisticsEntryType_FailedWriteCount, MsrStatisticsEntryType_GoodCardAuthenticationDataCount, MsrStatisticsEntryType_GoodDeviceAuthenticationCount, MsrStatisticsEntryType_GoodReadCount, MsrStatisticsEntryType_GoodWriteCount, MsrStatisticsEntryType_HoursPoweredCount, MsrStatisticsEntryType_Invalid, MsrStatisticsEntryType_MissingStartSentinelTrack1Count, MsrStatisticsEntryType_MissingStartSentinelTrack2Count, MsrStatisticsEntryType_MissingStartSentinelTrack3Count, MsrStatisticsEntryType_MissingStartSentinelTrack4Count, MsrStatisticsEntryType_ParityLRCErrorTrack1Count, MsrStatisticsEntryType_ParityLRCErrorTrack2Count, MsrStatisticsEntryType_ParityLRCErrorTrack3Count, MsrStatisticsEntryType_ParityLRCErrorTrack4Count, MsrStatisticsEntryType_UnreadableCardCount, MstStatisticsEntryType, MstStatisticsEntryType enumeration, _MsrStatisticsEntryType, pointofservicedriverinterface/MsrStatisticsEntryType_ChallengeRequestCount, pointofservicedriverinterface/MsrStatisticsEntryType_CommunicationErrorCount, pointofservicedriverinterface/MsrStatisticsEntryType_Count, pointofservicedriverinterface/MsrStatisticsEntryType_FailedCardAuthenticationDataCount, pointofservicedriverinterface/MsrStatisticsEntryType_FailedDeviceAuthenticationCount, pointofservicedriverinterface/MsrStatisticsEntryType_FailedReadCount, pointofservicedriverinterface/MsrStatisticsEntryType_FailedWriteCount, pointofservicedriverinterface/MsrStatisticsEntryType_GoodCardAuthenticationDataCount, pointofservicedriverinterface/MsrStatisticsEntryType_GoodDeviceAuthenticationCount, pointofservicedriverinterface/MsrStatisticsEntryType_GoodReadCount, pointofservicedriverinterface/MsrStatisticsEntryType_GoodWriteCount, pointofservicedriverinterface/MsrStatisticsEntryType_HoursPoweredCount, pointofservicedriverinterface/MsrStatisticsEntryType_Invalid, pointofservicedriverinterface/MsrStatisticsEntryType_MissingStartSentinelTrack1Count, pointofservicedriverinterface/MsrStatisticsEntryType_MissingStartSentinelTrack2Count, pointofservicedriverinterface/MsrStatisticsEntryType_MissingStartSentinelTrack3Count, pointofservicedriverinterface/MsrStatisticsEntryType_MissingStartSentinelTrack4Count, pointofservicedriverinterface/MsrStatisticsEntryType_ParityLRCErrorTrack1Count, pointofservicedriverinterface/MsrStatisticsEntryType_ParityLRCErrorTrack2Count, pointofservicedriverinterface/MsrStatisticsEntryType_ParityLRCErrorTrack3Count, pointofservicedriverinterface/MsrStatisticsEntryType_ParityLRCErrorTrack4Count, pointofservicedriverinterface/MsrStatisticsEntryType_UnreadableCardCount, pointofservicedriverinterface/MstStatisticsEntryType, pos.mststatisticsentrytype
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
req.irql: Called at PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pointofservicedriverinterface.h
api_name:
-	MstStatisticsEntryType
product: Windows
targetos: Windows
req.typenames: MstStatisticsEntryType
---

# _MsrStatisticsEntryType Enumeration
This enumeration defines the kinds of magnetic stripe reader statistics.

## Syntax
```
typedef enum _MsrStatisticsEntryType {
  MsrStatisticsEntryType_Invalid                            ,
  MsrStatisticsEntryType_HoursPoweredCount                  ,
  MsrStatisticsEntryType_CommunicationErrorCount            ,
  MsrStatisticsEntryType_GoodReadCount                      ,
  MsrStatisticsEntryType_FailedReadCount                    ,
  MsrStatisticsEntryType_UnreadableCardCount                ,
  MsrStatisticsEntryType_GoodWriteCount                     ,
  MsrStatisticsEntryType_FailedWriteCount                   ,
  MsrStatisticsEntryType_MissingStartSentinelTrack1Count    ,
  MsrStatisticsEntryType_ParityLRCErrorTrack1Count          ,
  MsrStatisticsEntryType_MissingStartSentinelTrack2Count    ,
  MsrStatisticsEntryType_ParityLRCErrorTrack2Count          ,
  MsrStatisticsEntryType_MissingStartSentinelTrack3Count    ,
  MsrStatisticsEntryType_ParityLRCErrorTrack3Count          ,
  MsrStatisticsEntryType_MissingStartSentinelTrack4Count    ,
  MsrStatisticsEntryType_ParityLRCErrorTrack4Count          ,
  MsrStatisticsEntryType_GoodCardAuthenticationDataCount    ,
  MsrStatisticsEntryType_FailedCardAuthenticationDataCount  ,
  MsrStatisticsEntryType_ChallengeRequestCount              ,
  MsrStatisticsEntryType_GoodDeviceAuthenticationCount      ,
  MsrStatisticsEntryType_FailedDeviceAuthenticationCount    ,
  MsrStatisticsEntryType_Count
} MstStatisticsEntryType;
```

## Constants

<table>
            
                <tr>
                    <td>MsrStatisticsEntryType_Invalid</td>
                    <td>Reserved for internal use.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_HoursPoweredCount</td>
                    <td>Number of hours that the device has been powered on.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_CommunicationErrorCount</td>
                    <td>Number of communication errors.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_GoodReadCount</td>
                    <td>Number of successful reads</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_FailedReadCount</td>
                    <td>Number of failed reads</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_UnreadableCardCount</td>
                    <td>Number of unreadable cards</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_GoodWriteCount</td>
                    <td>Number of successful writes. Do not use.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_FailedWriteCount</td>
                    <td>Number of failed writes. Do not use.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_MissingStartSentinelTrack1Count</td>
                    <td>Number of missing start sentinel errors on track 1. May indicate an empty track.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_ParityLRCErrorTrack1Count</td>
                    <td>Number of Parity or LRC errors on track 1</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_MissingStartSentinelTrack2Count</td>
                    <td>Number of missing start sentinel errors on track 2. May indicate an empty track.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_ParityLRCErrorTrack2Count</td>
                    <td>Number of Parity or LRC errors on track 2</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_MissingStartSentinelTrack3Count</td>
                    <td>Number of missing start sentinel errors on track 3. May indicate an empty track.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_ParityLRCErrorTrack3Count</td>
                    <td>Number of Parity or LRC errors on track 3</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_MissingStartSentinelTrack4Count</td>
                    <td>Number of missing start sentinel errors on track 4. May indicate an empty track.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_ParityLRCErrorTrack4Count</td>
                    <td>Number of Parity or LRC errors on track 4</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_GoodCardAuthenticationDataCount</td>
                    <td>Number of successful card authentication data reads</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_FailedCardAuthenticationDataCount</td>
                    <td>Number of failed card authentication data reads</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_ChallengeRequestCount</td>
                    <td>Number of successful calls to <a href="https://msdn.microsoft.com/f94ce49d-ab87-4d8f-8fc7-af8899b37ca1">RetrieveDeviceAuthenticationDataAsync</a>.</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_GoodDeviceAuthenticationCount</td>
                    <td>Number of successful card authentication attempts</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_FailedDeviceAuthenticationCount</td>
                    <td>Number of failed card authentication attempts</td>
                </tr>
            
                <tr>
                    <td>MsrStatisticsEntryType_Count</td>
                    <td>Count of entry types</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |