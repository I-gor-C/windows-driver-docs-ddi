---
UID: NF.d3dkmthk.D3DKMTReleaseKeyedMutex2
title: D3DKMTReleaseKeyedMutex2 function
author: windows-driver-content
description: Releases a keyed mutex object that includes private data.
old-location: display\d3dkmtreleasekeyedmutex2.htm
old-project: display
ms.assetid: e5df165c-3d85-42b9-affe-3dcc7c46aa0b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTReleaseKeyedMutex2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTReleaseKeyedMutex2
req.alt-loc: Gdi32.dll,API-MS-Win-dx-d3dkmt-l1-1-0.dll,API-MS-Win-dx-d3dkmt-l1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
---

# D3DKMTReleaseKeyedMutex2 function



## -description
Releases a keyed mutex object that includes private data.


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTReleaseKeyedMutex2(
  _Inout_ D3DKMT_RELEASEKEYEDMUTEX2 *pData
);
````


## -parameters

### -param pData [in, out]

A pointer to a <a href="display.d3dkmt_releasekeyedmutex2">D3DKMT_RELEASEKEYEDMUTEX2</a> structure that specifies the keyed mutex object to release. 

## -returns
Returns one of the following values.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The keyed mutex object was successfully released. 
<dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl>The graphics adapter was stopped or the display device was reset.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.
<dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl>
<a href="display.d3dkmtreleasekeyedmutex2">D3DKMTReleaseKeyedMutex2</a> could not complete because of insufficient memory.

 

This function might also return other NTSTATUS values.

## -remarks
<b>D3DKMTReleaseKeyedMutex2</b> behaves like 
  the <a href="display.d3dkmtreleasekeyedmutex">D3DKMTReleaseKeyedMutex</a> function but lets 
  the caller specify private data to associate with the keyed mutex.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
</td>
</tr>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_releasekeyedmutex2">D3DKMT_RELEASEKEYEDMUTEX2</a>
</dt>
<dt>
<a href="display.d3dkmtreleasekeyedmutex">D3DKMTReleaseKeyedMutex</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTReleaseKeyedMutex2 function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
