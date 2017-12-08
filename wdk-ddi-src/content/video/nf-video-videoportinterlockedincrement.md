---
UID: NF.video.VideoPortInterlockedIncrement
title: VideoPortInterlockedIncrement function
author: windows-driver-content
description: The VideoPortInterlockedIncrement function increments a caller-supplied variable as an atomic operation.
old-location: display\videoportinterlockedincrement.htm
old-project: display
ms.assetid: d3507214-82bc-4d73-8562-2843d7876137
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: VideoPortInterlockedIncrement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortInterlockedIncrement
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: Any level
req.product: Windows 10 or later.
---

# VideoPortInterlockedIncrement function



## -description
The <b>VideoPortInterlockedIncrement</b> function increments a caller-supplied variable as an atomic operation.


## -syntax

````
LONG FASTCALL VideoPortInterlockedIncrement(
  _In_ PLONG Addend
);
````


## -parameters

### -param Addend [in]

Pointer to the variable to be incremented.

## -returns
<b>VideoPortInterlockedIncrement</b> returns the incremented value.

## -remarks
When possible and whenever appropriate, <b>VideoPortInterlockedIncrement</b> is implemented inline by the compiler. It can be safely used on pageable data.

This function is atomic only with respect to other <b>VideoPortInterlocked</b><i>Xxx</i> calls. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows 2000 and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.videoportinterlockeddecrement">VideoPortInterlockedDecrement</a>
</dt>
<dt>
<a href="display.videoportinterlockedexchange">VideoPortInterlockedExchange</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortInterlockedIncrement function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
