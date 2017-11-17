---
UID: NE.wdm._LOCK_OPERATION
title: LOCK_OPERATION
author: windows-driver-content
description: The LOCK_OPERATION enumeration specifies the type of access that is appropriate for a type of I/O operation.
old-location: ifsk\lock_operation.htm
ms.assetid: 25b2dd6a-2e20-4221-bef4-0001bbaae1d5
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: ifsk
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LOCK_OPERATION
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# LOCK_OPERATION enumeration



## -description
<p>The <b>LOCK_OPERATION</b> enumeration specifies the type of access that is appropriate for a type of I/O operation.</p>


## -syntax

````
typedef enum  { 
  IoReadAccess,
  IoWriteAccess,
  IoModifyAccess
} LOCK_OPERATION;
````


## -enum-fields
<dl>

### -field <a id="IoReadAccess"></a><a id="ioreadaccess"></a><a id="IOREADACCESS"></a><b>IoReadAccess</b>

<dd>
<p>This value indicates that a driver  can examine the contents of a buffer but cannot change the contents.</p>
</dd>

### -field <a id="IoWriteAccess"></a><a id="iowriteaccess"></a><a id="IOWRITEACCESS"></a><b>IoWriteAccess</b>

<dd>
<p>This value indicates that a driver can examine and change the contents of a buffer. </p>
</dd>

### -field <a id="IoModifyAccess"></a><a id="iomodifyaccess"></a><a id="IOMODIFYACCESS"></a><b>IoModifyAccess</b>

<dd>
<p>This value indicates that a driver can examine and change the contents of a buffer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541956">FltDecodeParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554664">MmProbeAndLockPages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20LOCK_OPERATION enumeration%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
