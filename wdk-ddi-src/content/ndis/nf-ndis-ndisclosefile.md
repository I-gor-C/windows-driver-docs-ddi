---
UID: NF.ndis.NdisCloseFile
title: NdisCloseFile function
author: windows-driver-content
description: The NdisCloseFile function releases a handle returned by the NdisOpenFile function and frees the memory allocated to hold the file contents when it was opened.
old-location: netvista\ndisclosefile.htm
old-project: NetVista
ms.assetid: a12f7597-cfe7-466f-a5b5-aafd885d5adf
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisCloseFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisCloseFile (NDIS 5.1)) in Windows   Vista. Supported for NDIS 5.1 drivers (see    NdisCloseFile (NDIS 5.1)) in Windows   XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCloseFile
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NdisCloseFile function



## -description
The 
  <b>NdisCloseFile</b> function releases a handle returned by the 
  <a href="netvista.ndisopenfile">NdisOpenFile</a> function and frees the memory
  allocated to hold the file contents when it was opened.



## -syntax

````
VOID NdisCloseFile(
  _In_ NDIS_HANDLE FileHandle
);
````


## -parameters

### -param FileHandle [in]

The handle that was returned in a preceding call to the 
     <a href="netvista.ndisopenfile">NdisOpenFile</a> function.


## -returns
None


## -remarks
For miniport drivers, calls to this function are valid only during initialization. If the 
    <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function
    calls the 
    <a href="netvista.ndisopenfile">NdisOpenFile</a> function, it must call 
    <b>NdisCloseFile</b> before it returns control.


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
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff550912">NdisCloseFile (NDIS 5.1)</a>) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCloseFile (NDIS 5.1)</b>) in Windows
   XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndismapfile">NdisMapFile</a>
</dt>
<dt>
<a href="netvista.ndisopenfile">NdisOpenFile</a>
</dt>
<dt>
<a href="netvista.ndisunmapfile">NdisUnmapFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisCloseFile function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

