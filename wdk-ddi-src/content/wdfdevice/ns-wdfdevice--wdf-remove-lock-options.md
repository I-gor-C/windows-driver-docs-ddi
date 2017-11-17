---
UID: NS.wdfdevice._WDF_REMOVE_LOCK_OPTIONS
title: WDF_REMOVE_LOCK_OPTIONS
author: windows-driver-content
description: The WDF_REMOVE_LOCK_OPTIONS structure specifies options for acquiring a remove lock before delivering an IRP to the driver.
old-location: wdf\wdf_remove_lock_options.htm
ms.assetid: 0A50C1FB-D0C6-47C4-AD71-AD0B7486AA2E
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_REMOVE_LOCK_OPTIONS
req.alt-loc: wdfdevice.h
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
ms.keywords: WDF_REMOVE_LOCK_OPTIONS, WDF_REMOVE_LOCK_OPTIONS, *PWDF_REMOVE_LOCK_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REMOVE_LOCK_OPTIONS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The <b>WDF_REMOVE_LOCK_OPTIONS</b> structure specifies options for acquiring a remove lock before delivering an IRP to the driver.</p>


## -syntax

````
typedef struct _WDF_REMOVE_LOCK_OPTIONS {
  ULONG Size;
  ULONG Flags;
} WDF_REMOVE_LOCK_OPTIONS, *PWDF_REMOVE_LOCK_OPTIONS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of the structure, in bytes.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The bitwise <b>OR</b> of values from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406498">WDF_REMOVE_LOCK_OPTIONS_FLAGS</a> enumeration.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451095">WdfDeviceInitSetRemoveLockOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406501">WDF_REMOVE_LOCK_OPTIONS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406498">WDF_REMOVE_LOCK_OPTIONS_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REMOVE_LOCK_OPTIONS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
