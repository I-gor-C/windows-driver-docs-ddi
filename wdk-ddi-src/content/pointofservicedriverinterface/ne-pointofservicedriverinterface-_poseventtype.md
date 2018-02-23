---
UID: NE:pointofservicedriverinterface._PosEventType
title: "_PosEventType"
author: windows-driver-content
description: This enumeration defines values used in the PosEventDataHeader structure to indicate the type of event that was raised.
old-location: pos\poseventtype.htm
old-project: pos
ms.assetid: 2ba0c81f-2eff-48bf-8c3e-9047a398f735
ms.author: windowsdriverdev
ms.date: 2/19/2018
ms.keywords: MagneticStripeReaderDataReceived, pointofservicedriverinterface/BarcodeScannerDataReceived, pointofservicedriverinterface/BarcodeScannerErrorOccurred, AlarmTimeoutExpired, _PosEventType, pointofservicedriverinterface/BarcodeScannerImagePreviewReceived, ReleaseDeviceRequested, StatusUpdated, InvalidEvent, PosEventType, BarcodeScannerErrorOccurred, pointofservicedriverinterface/AlarmTimeoutExpired, pointofservicedriverinterface/_Max, pointofservicedriverinterface/BarcodeScannerTriggerPressed, pointofservicedriverinterface/MagneticStripeReaderErrorOccurred, pointofservicedriverinterface/DrawerOpened, pointofservicedriverinterface/DrawerClosed, BarcodeScannerTriggerReleased, pointofservicedriverinterface/PosEventType, pointofservicedriverinterface/BarcodeScannerTriggerReleased, PosEventType enumeration, DrawerClosed, PointOfServicePrinterErrorOccurred, pointofservicedriverinterface/InvalidEvent, pos.poseventtype, MagneticStripeReaderErrorOccurred, pointofservicedriverinterface/MagneticStripeReaderDataReceived, DrawerOpened, pointofservicedriverinterface/ReleaseDeviceRequested, pointofservicedriverinterface/PointOfServicePrinterErrorOccurred, _Max, BarcodeScannerImagePreviewReceived, BarcodeScannerTriggerPressed, BarcodeScannerDataReceived, pointofservicedriverinterface/StatusUpdated
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	pointofservicedriverinterface.h
apiname:
-	PosEventType
product: Windows
targetos: Windows
req.typenames: PosEventType
---

# _PosEventType Enumeration
This enumeration defines values used in the <a href="..\pointofservicedriverinterface\ns-pointofservicedriverinterface-_poseventdataheader.md">PosEventDataHeader</a> structure to indicate the type of event that was raised.

## Syntax
````
typedef enum _PosEventType { 
  InvalidEvent                        = 0,
  ReleaseDeviceRequested              = 1,
  StatusUpdated                       = 2,
  BarcodeScannerTriggerPressed        = 3,
  BarcodeScannerTriggerReleased       = 4,
  BarcodeScannerDataReceived          = 5,
  BarcodeScannerErrorOccurred         = 6,
  BarcodeScannerImagePreviewReceived  = 7,
  MagneticStripeReaderDataReceived    = 8,
  MagneticStripeReaderErrorOccurred   = 9,
  PointOfServicePrinterErrorOccurred  = 10,
  AlarmTimeoutExpired                 = 11,
  DrawerClosed                        = 12,
  DrawerOpened                        = 13,
  _Max                                = 14
} PosEventType;
````

## Constants

<table>
            
                <tr>
                    <td>_Max</td>
                    <td>Represents the _Max event.</td>
                </tr>
            
                <tr>
                    <td>_MinEventType</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>AlarmTimeoutExpired</td>
                    <td>Represents the AlarmTimeoutExpired event.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerDataReceived</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757463">BarcodeScannerDataReceived</a> event.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerErrorOccurred</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757464">BarcodeScannerErrorOccurred</a> event.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerImagePreviewReceived</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757466">BarcodeScannerImagePreviewReceived</a> event.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerTriggerPressed</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757468">BarcodeScannerTriggerPressed</a> event.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerTriggerReleased</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn757469">BarcodeScannerTriggerReleased</a> event.</td>
                </tr>
            
                <tr>
                    <td>DrawerClosed</td>
                    <td>Represents the DrawerClosed event.</td>
                </tr>
            
                <tr>
                    <td>DrawerOpened</td>
                    <td>Represents the DrawerOpened event.</td>
                </tr>
            
                <tr>
                    <td>InvalidEvent</td>
                    <td>The event code is not valid.</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderDataReceived</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn772149">MagneticStripeReaderDataReceived</a> event.</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderErrorOccurred</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn772151">MagneticStripeReaderErrorOccured</a> event.</td>
                </tr>
            
                <tr>
                    <td>PointOfServicePrinterErrorOccurred</td>
                    <td>Represents the PointOfServicePrinterErrorOccurred event.</td>
                </tr>
            
                <tr>
                    <td>ReleaseDeviceRequested</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn790033">ReleaseDeviceRequested</a> event.</td>
                </tr>
            
                <tr>
                    <td>StatusUpdated</td>
                    <td>Represents the <a href="https://msdn.microsoft.com/library/windows/hardware/dn790040">StatusUpdated</a> event.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |