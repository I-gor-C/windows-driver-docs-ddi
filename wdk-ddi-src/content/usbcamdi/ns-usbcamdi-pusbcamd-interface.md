---
UID: NS.usbcamdi.PUSBCAMD_INTERFACE
title: PUSBCAMD_INTERFACE
author: windows-driver-content
description: The USBCAMD_INTERFACE structure defines a set of services related to the USB bus interfaces.
old-location: stream\usbcamd_interface.htm
old-project: stream
ms.assetid: 864dbe8d-2771-4532-8a50-ed1bf5286658
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PUSBCAMD_INTERFACE, USBCAMD_INTERFACE, *PUSBCAMD_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_INTERFACE
req.alt-loc: usbcamdi.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PUSBCAMD_INTERFACE structure



## -description
<p>The USBCAMD_INTERFACE structure defines a set of services related to the USB bus interfaces.</p>


## -syntax

````
typedef struct {
  INTERFACE                      Interface;
  PFNUSBCAMD_WaitOnDeviceEvent   USBCAMD_WaitOnDeviceEvent;
  PFNUSBCAMD_BulkReadWrite       USBCAMD_BulkReadWrite;
  PFNUSBCAMD_SetVideoFormat      USBCAMD_SetVideoFormat;
  PFNUSBCAMD_SetIsoPipeState     USBCAMD_SetIsoPipeState;
  PFNUSBCAMD_CancelBulkReadWrite USBCAMD_CancelBulkReadWrite;
} USBCAMD_INTERFACE, *PUSBCAMD_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Interface</b>

<dd>
<p>Describes the interface that USBCAMD exports for use by other drivers.</p>
</dd>

### -field <b>USBCAMD_WaitOnDeviceEvent</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="stream.usbcamd_waitondeviceevent">USBCAMD_WaitOnDeviceEvent</a> service.</p>
</dd>

### -field <b>USBCAMD_BulkReadWrite</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="stream.usbcamd_bulkreadwrite">USBCAMD_BulkReadWrite</a> service.</p>
</dd>

### -field <b>USBCAMD_SetVideoFormat</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="stream.usbcamd_setvideoformat">USBCAMD_SetVideoFormat</a> service.</p>
</dd>

### -field <b>USBCAMD_SetIsoPipeState</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="stream.usbcamd_setisopipestate">USBCAMD_SetIsoPipeState</a> service.</p>
</dd>

### -field <b>USBCAMD_CancelBulkReadWrite</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="stream.usbcamd_cancelbulkreadwrite">USBCAMD_CancelBulkReadWrite</a> service.</p>
</dd>
</dl>

## -remarks
<p>The camera minidriver may obtain the USBCAMD_INTERFACE entry points at any point after it has received <a href="https://msdn.microsoft.com/library/windows/hardware/ff568182">SRB_INITIALIZATION_COMPLETE</a>. The IRP for acquiring a USBCAMD_INTERFACE is <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> and must be sent at IRQL = PASSIVE_LEVEL. Typically, a camera minidriver obtains the addresses of the USBCAMD_INTERFACE entry points once toward the end of the initialization of the camera minidriver. The members of the USBCAMD_INTERFACE structure are filled with the minidriver's entry points as described in <a href="NULL">Acquiring USBCAMD2 Features</a>
</p>

<p><b>USBCAMD_INTERFACE</b> is not supported in the original USBCAMD.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
<dt>
<a href="stream.usbcamd_waitondeviceevent">USBCAMD_WaitOnDeviceEvent</a>
</dt>
<dt>
<a href="stream.usbcamd_bulkreadwrite">USBCAMD_BulkReadWrite</a>
</dt>
<dt>
<a href="stream.usbcamd_setvideoformat">USBCAMD_SetVideoFormat</a>
</dt>
<dt>
<a href="stream.usbcamd_setisopipestate">USBCAMD_SetIsoPipeState</a>
</dt>
<dt>
<a href="stream.usbcamd_cancelbulkreadwrite">USBCAMD_CancelBulkReadWrite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568182">SRB_INITIALIZATION_COMPLETE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_INTERFACE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
