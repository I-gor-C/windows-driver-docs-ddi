---
UID: NE.urstypes._URS_HARDWARE_EVENT
title: _URS_HARDWARE_EVENT
author: windows-driver-content
description: Defines values for the hardware events that a client driver for a USB dual-role controller can report.
old-location: buses\urs_hardware_event.htm
old-project: usbref
ms.assetid: 985A7725-1EE1-4419-B8BE-FEE2306E93A7
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _URS_HARDWARE_EVENT, URS_HARDWARE_EVENT, *PURS_HARDWARE_EVENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: urstypes.h
req.include-header: Urscx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: URS_HARDWARE_EVENT, *PURS_HARDWARE_EVENT
req.alt-loc: Urstypes.h
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
req.product: Windows 10 or later.
---

# _URS_HARDWARE_EVENT enumeration



## -description
Defines values for the hardware events that a client driver for a USB dual-role controller can report.


## -syntax

````
typedef enum _URS_HARDWARE_EVENT { 
  UrsHardwareEventNone         = 0,
  UrsHardwareEventDetach,
  UrsHardwareEventIdGround,
  UrsHardwareEventIdFloat,
  UrsHardwareEventPortTypeDfp,
  UrsHardwareEventPortTypeUfp
} URS_HARDWARE_EVENT, *PURS_HARDWARE_EVENT;
````


## -enum-fields

### -field UrsHardwareEventNone

Internal use only. 

### -field UrsHardwareEventDetach

A detach event occurred on a port of a USB Type-C system. 

### -field UrsHardwareEventIdGround

This event indicates that the ID pin is grounded.

### -field UrsHardwareEventIdFloat

This event indicates that the ID pin is floating.

### -field UrsHardwareEventPortTypeDfp

The Type-C connector has resolved to DFP. Not to be used directly by the URS client driver.

### -field UrsHardwareEventPortTypeUfp

The Type-C connector has resolved to UFP. Not to be used directly by the URS client driver.

## -remarks
Values defined for USB Type-C systems should not be directly used by the client driver. Instead the driver should report that it does not support hardware event reporting by calling <a href="buses.urssethardwareeventsupport">UrsSetHardwareEventSupport</a>. These hardware events are detected by a USB Type-C connector driver, see <a href="buses.usb_connection_manager_class_extension__ucmcx_">USB Type-C connector driver programming reference</a>. 

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.15
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Urstypes.h (include Urscx.h)</dt>
</dl>
</td>
</tr>
</table>