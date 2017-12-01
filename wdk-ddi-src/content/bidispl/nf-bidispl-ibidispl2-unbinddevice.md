---
UID: NF.bidispl.IBidiSpl2.UnbindDevice
title: IBidiSpl2::UnbindDevice
author: windows-driver-content
description: The IBidiSpl2::UnbindDevice method releases a printer from a bidirectional printer communication (bidi communication) request.
old-location: print\ibidispl2_ibidispl2__unbinddevice.htm
old-project: print
ms.assetid: 26f3fc82-051d-4827-8b59-ac2c99f4d2c5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: bidispl.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiSpl2.IBidiSpl2::UnbindDevice
req.alt-loc: bidispl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Bidispl.dll
req.irql: PASSIVE_LEVEL
req.iface: IBidiSpl2
---

# IBidiSpl2::UnbindDevice method



## -description
<p>The <b>IBidiSpl2::UnbindDevice</b> method releases a printer from a bidirectional printer communication (bidi communication) request.</p>


## -syntax

````
HRESULT IBidiSpl2::UnbindDevice();
````


## -parameters


## -returns
<p>The method returns one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>E_HANDLE</b></dt>
</dl><p>The interface handle is invalid.</p><dl>
<dt><b>None of the above</b></dt>
</dl><p>The <b>HRESULT</b> contains an error code that corresponds to the last error.</p>

<p> </p>

<p>The method returns one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>E_HANDLE</b></dt>
</dl><p>The interface handle is invalid.</p><dl>
<dt><b>None of the above</b></dt>
</dl><p>The <b>HRESULT</b> contains an error code that corresponds to the last error.</p>

<p> </p>

<p>The method returns one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>E_HANDLE</b></dt>
</dl><p>The interface handle is invalid.</p><dl>
<dt><b>None of the above</b></dt>
</dl><p>The <b>HRESULT</b> contains an error code that corresponds to the last error.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bidispl.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Bidispl.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bidispl\nn-bidispl-ibidispl2.md">IBidiSpl2</a>
</dt>
<dt>
<a href="print.bidirectional_communication_interfaces">Bidirectional Communication Interfaces</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/42b5e6cf-b434-4734-86f3-b3b9d15ea468">Print Spooler Components</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2::IBidiSpl2::UnbindDevice method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
