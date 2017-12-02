---
UID: NC.ufxproprietarycharger.UFX_PROPRIETARY_CHARGER_ABORT_OPERATION
title: UFX_PROPRIETARY_CHARGER_ABORT_OPERATION
author: windows-driver-content
description: The filter driver's implementation to abort a charger operation.
old-location: buses\ufx_proprietary_charger_abort_operation.htm
old-project: usbref
ms.assetid: 32BCBE1C-BD0E-46D6-9C6D-6B8F1CE0E540
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_ENDPOINT_CALLBACKS, UFX_ENDPOINT_CALLBACKS, *PUFX_ENDPOINT_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ufxproprietarycharger.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PFN_UFX_PROPRIETARY_CHARGER_ABORT_OPERATION
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UFX_PROPRIETARY_CHARGER_ABORT_OPERATION callback



## -description
<p>The filter driver's implementation to abort a charger operation.</p>


## -prototype

````
UFX_PROPRIETARY_CHARGER_ABORT_OPERATION UfxProprietaryChargerAbort;

NTSTATUS UfxProprietaryChargerAbort(
  _In_ PVOID Context
)
{ ... }

typedef UFX_PROPRIETARY_CHARGER_ABORT_OPERATION PFN_UFX_PROPRIETARY_CHARGER_ABORT_OPERATION;
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>    A pointer to a driver-defined context.</p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>To support handling of proprietary chargers, the USB lower filter driver must publish support. During the publishing process, the driver also registers its implementation of this  callback function. For more information, see <a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxproprietarycharger.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UFX_PROPRIETARY_CHARGER_ABORT_OPERATION callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
