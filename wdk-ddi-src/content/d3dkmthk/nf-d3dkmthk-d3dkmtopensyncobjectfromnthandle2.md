---
UID: NF.d3dkmthk.D3DKMTOpenSyncObjectFromNtHandle2
title: D3DKMTOpenSyncObjectFromNtHandle2 function
author: windows-driver-content
description: D3DKMTOpenSyncObjectFromNtHandle2 opens a monitored fence object from an NT handle previously created by D3DKMTShareObjects.
old-location: display\d3dkmtopensyncobjectfromnthandle2.htm
old-project: display
ms.assetid: E3295F4F-AB51-4EBB-8B9F-E47BBA52AF47
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3DKMTOpenSyncObjectFromNtHandle2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTOpenSyncObjectFromNtHandle2
req.alt-loc: GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: GDI32.lib
req.dll: GDI32.dll
req.irql: 
---

# D3DKMTOpenSyncObjectFromNtHandle2 function



## -description
<b>D3DKMTOpenSyncObjectFromNtHandle2</b> opens a monitored fence object from an NT handle previously created by <a href="display.d3dkmtshareobjects">D3DKMTShareObjects</a>.



## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTOpenSyncObjectFromNtHandle2(
  _Inout_ D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 *pData
);
````


## -parameters

### -param pData [in, out]

A pointer to a <a href="display.d3dkmt_opensyncobjectfromnthandle2">D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2</a> structure that describes the operation.


## -returns
Returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation was performed successfully.
<dl>
<dt><b>STATUS_INVALID_PARAMETER </b></dt>
</dl>
         Parameters were validated and determined to be incorrect.

 

This function might also return other <b>NTSTATUS</b> values.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

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
<dt>GDI32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>GDI32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_opensyncobjectfromnthandle2">D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2</a>
</dt>
<dt>
<a href="display.d3dkmtshareobjects">D3DKMTShareObjects</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTOpenSyncObjectFromNtHandle2 function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

