---
UID: NF.d3dkmthk.D3DKMTQueryResourceInfoFromNtHandle
title: D3DKMTQueryResourceInfoFromNtHandle function
author: windows-driver-content
description: Maps a global NT handle to resource information that is needed for a call to the D3DKMTQueryResourceInfo function.
old-location: display\d3dkmtqueryresourceinfofromnthandle.htm
old-project: display
ms.assetid: 7a433aaf-3215-4d11-8989-2d7bdc7f7499
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTQueryResourceInfoFromNtHandle
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
req.alt-api: D3DKMTQueryResourceInfoFromNtHandle
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

# D3DKMTQueryResourceInfoFromNtHandle function



## -description
Maps a global NT handle  to resource information that is needed for a call to the <a href="display.d3dkmtqueryresourceinfo">D3DKMTQueryResourceInfo</a> function.


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTQueryResourceInfoFromNtHandle(
  _Inout_ D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE *pData
);
````


## -parameters

### -param pData [in, out]

A pointer to a <a href="display.d3dkmt_queryresourceinfofromnthandle">D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE</a> structure that describes information that is required to perform the mapping.

## -returns
Returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The mapping was performed successfully.
<dl>
<dt><b>STATUS_INVALID_PARAMETER </b></dt>
</dl>
         Parameters were validated and determined to be incorrect.

 

This function might also return other NTSTATUS values.

## -remarks


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
<a href="display.d3dkmt_queryresourceinfofromnthandle">D3DKMT_QUERYRESOURCEINFOFROMNTHANDLE</a>
</dt>
<dt>
<a href="display.d3dkmtqueryresourceinfo">D3DKMTQueryResourceInfo</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTQueryResourceInfoFromNtHandle function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
