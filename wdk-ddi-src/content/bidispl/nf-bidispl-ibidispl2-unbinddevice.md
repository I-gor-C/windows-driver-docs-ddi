---
UID: NF.bidispl.IBidiSpl2.UnbindDevice
title: IBidiSpl2::UnbindDevice method
author: windows-driver-content
description: The IBidiSpl2::UnbindDevice method releases a printer from a bidirectional printer communication (bidi communication) request.
old-location: print\ibidispl2_ibidispl2__unbinddevice.htm
old-project: print
ms.assetid: 26f3fc82-051d-4827-8b59-ac2c99f4d2c5
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IBidiSpl2, IBidiSpl2::UnbindDevice, UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
req.irql: 
---

# IBidiSpl2::UnbindDevice method



## -description
The <b>IBidiSpl2::UnbindDevice</b> method releases a printer from a bidirectional printer communication (bidi communication) request.



## -syntax

````
HRESULT IBidiSpl2::UnbindDevice();
````


## -parameters


## -returns
The method returns one of the following values.
<dl>
<dt><b>S_OK</b></dt>
</dl>The operation was successful.
<dl>
<dt><b>E_HANDLE</b></dt>
</dl>The interface handle is invalid.
<dl>
<dt><b>None of the above</b></dt>
</dl>The <b>HRESULT</b> contains an error code that corresponds to the last error.

 

The method returns one of the following values.
<dl>
<dt><b>S_OK</b></dt>
</dl>The operation was successful.
<dl>
<dt><b>E_HANDLE</b></dt>
</dl>The interface handle is invalid.
<dl>
<dt><b>None of the above</b></dt>
</dl>The <b>HRESULT</b> contains an error code that corresponds to the last error.

 

The method returns one of the following values.
<dl>
<dt><b>S_OK</b></dt>
</dl>The operation was successful.
<dl>
<dt><b>E_HANDLE</b></dt>
</dl>The interface handle is invalid.
<dl>
<dt><b>None of the above</b></dt>
</dl>The <b>HRESULT</b> contains an error code that corresponds to the last error.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows Vista

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2008

</td>
</tr>
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
Header

</th>
<td width="70%">
<dl>
<dt>Bidispl.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2::IBidiSpl2::UnbindDevice method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

