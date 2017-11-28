---
UID: NS.ufxproprietarycharger._UFX_INTERFACE_PROPRIETARY_CHARGER
title: UFX_INTERFACE_PROPRIETARY_CHARGER
author: windows-driver-content
description: Stores pointers to driver-implemented callback functions for handling proprietary charger operations.
old-location: buses\ufx_interface_proprietary_charger.htm
old-project: usbref
ms.assetid: 3E75EA87-FBF8-4FFB-9CD7-F8E1D5353D68
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_INTERFACE_PROPRIETARY_CHARGER, UFX_INTERFACE_PROPRIETARY_CHARGER, *PUFX_INTERFACE_PROPRIETARY_CHARGER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufxproprietarycharger.h
req.include-header: Ufxproprietarycharger.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFX_INTERFACE_PROPRIETARY_CHARGER
req.alt-loc: ufxproprietarycharger.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UFX_INTERFACE_PROPRIETARY_CHARGER structure



## -description
<p>Stores pointers to driver-implemented callback functions for handling proprietary charger operations.</p>


## -syntax

````
typedef struct _UFX_INTERFACE_PROPRIETARY_CHARGER {
  INTERFACE                                   InterfaceHeader;
  PFN_UFX_PROPRIETARY_CHARGER_DETECT          ProprietaryChargerDetect;
  PFN_UFX_PROPRIETARY_CHARGER_SET_PROPERTY    ProprietaryChargerSetProperty;
  PFN_UFX_PROPRIETARY_CHARGER_ABORT_OPERATION ProprietaryChargerAbortOperation;
  PFN_UFX_PROPRIETARY_CHARGER_RESET_OPERATION ProprietaryChargerResetOperation;
} UFX_INTERFACE_PROPRIETARY_CHARGER, *PUFX_INTERFACE_PROPRIETARY_CHARGER;
````


## -struct-fields
<dl>

### -field <b>InterfaceHeader</b>

<dd>
<p>The interface version number.</p>
</dd>

### -field <b>ProprietaryChargerDetect</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187981">UFX_PROPRIETARY_CHARGER_DETECT</a> callback function.</p>
</dd>

### -field <b>ProprietaryChargerSetProperty</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187983">UFX_PROPRIETARY_CHARGER_SET_PROPERTY</a> callback function.</p>
</dd>

### -field <b>ProprietaryChargerAbortOperation</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187980">UFX_PROPRIETARY_CHARGER_ABORT_OPERATION</a> callback function.</p>
</dd>

### -field <b>ProprietaryChargerResetOperation</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187982">UFX_PROPRIETARY_CHARGER_RESET_OPERATION</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxproprietarycharger.h (include Ufxproprietarycharger.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UFX_INTERFACE_PROPRIETARY_CHARGER structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
