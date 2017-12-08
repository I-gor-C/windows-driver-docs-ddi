---
UID: NF.ks.KsReleaseDeviceSecurityLock
title: KsReleaseDeviceSecurityLock function
author: windows-driver-content
description: The KsReleaseDeviceSecurityLock function releases a previously acquired security lock on the device object header.
old-location: stream\ksreleasedevicesecuritylock.htm
old-project: stream
ms.assetid: b14a4816-2e72-491d-9881-ae532c287e99
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsReleaseDeviceSecurityLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsReleaseDeviceSecurityLock
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
---

# KsReleaseDeviceSecurityLock function



## -description
The <b>KsReleaseDeviceSecurityLock</b> function releases a previously acquired security lock on the device object header.


## -syntax

````
VOID KsReleaseDeviceSecurityLock(
  _In_ KSDEVICE_HEADER Header
);
````


## -parameters

### -param Header [in]

Points to a header previously allocated by <b>KsAllocateDeviceHeader</b> whose security lock is to be released.

## -returns
None

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksallocatedeviceheader">KsAllocateDeviceHeader</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsReleaseDeviceSecurityLock function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
