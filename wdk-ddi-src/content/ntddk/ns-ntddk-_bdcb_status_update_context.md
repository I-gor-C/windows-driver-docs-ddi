---
UID: NS.NTDDK._BDCB_STATUS_UPDATE_CONTEXT
title: _BDCB_STATUS_UPDATE_CONTEXT
author: windows-driver-content
description: The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's BOOT_DRIVER_CALLBACK_FUNCTION routine.
old-location: kernel\bdcb_status_update_context.htm
old-project: kernel
ms.assetid: 5DB29B81-2D7A-44FA-B5A9-FEF87C6A926D
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _BDCB_STATUS_UPDATE_CONTEXT, *PBDCB_STATUS_UPDATE_CONTEXT, BDCB_STATUS_UPDATE_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDCB_STATUS_UPDATE_CONTEXT
req.alt-loc: ntddk.h
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
---

# _BDCB_STATUS_UPDATE_CONTEXT structure



## -description
The BDCB_STATUS_UPDATE_CONTEXT structure describes a status update provided by Windows to a boot-start driver's <a href="kernel.ioregisterbootdrivercallback">BOOT_DRIVER_CALLBACK_FUNCTION</a> routine.



## -syntax

````
typedef struct _BDCB_STATUS_UPDATE_CONTEXT {
  BDCB_STATUS_UPDATE_TYPE StatusType;
} BDCB_STATUS_UPDATE_CONTEXT, *PBDCB_STATUS_UPDATE_CONTEXT;
````


## -struct-fields

### -field StatusType

The type of the status update.


## -remarks
Boot-start drivers must not unregister their boot-start driver callbacks during a callback. Doing so may result in a bug check. To properly unregister a boot-driver callback, boot-start drivers must specify an <a href="kernel.unload">Unload</a> routine in their <a href="kernel.driver_object">driver object</a> and call <a href="kernel.iounregisterbootdrivercallback">IoUnRegisterBootDriverCallback</a> from within the Unload dispatch routine.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with  Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioregisterbootdrivercallback">BOOT_DRIVER_CALLBACK_FUNCTION</a>
</dt>
<dt>
<a href="kernel.bdcb_status_update_type">BDCB_STATUS_UPDATE_TYPE</a>
</dt>
<dt>
<a href="kernel.iounregisterbootdrivercallback">IoUnRegisterBootDriverCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BDCB_STATUS_UPDATE_CONTEXT structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

