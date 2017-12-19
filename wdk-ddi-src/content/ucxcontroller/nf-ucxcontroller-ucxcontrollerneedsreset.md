---
UID: NF.ucxcontroller.UcxControllerNeedsReset
title: UcxControllerNeedsReset function
author: windows-driver-content
description: Initiates a non-Plug and Play (PnP) controller reset operation by queuing an event into the controller reset state machine.
old-location: buses\_ucxcontrollerneedsreset.htm
old-project: UsbRef
ms.assetid: FAE099E4-6BE9-4637-934F-9F86FFDCAA6A
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: UcxControllerNeedsReset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: UcxControllerNeedsReset
req.alt-loc: Ucxcontroller.h
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
req.product: Windows 10 or later.
---

# UcxControllerNeedsReset function



## -description
Initiates a non-Plug and Play (PnP) controller reset operation by queuing an event 
        into the controller reset state machine.




## -syntax

````
BOOL UcxControllerNeedsReset(
  [in] UCXCONTROLLER Controller
);
````


## -parameters

### -param Controller [in]

A handle to the controller object to reset. The client driver retrieved the handle in a previous call to <a href="buses._ucxcontrollercreate">UcxControllerCreate</a>.


## -returns
If the operation is successful, the method returns TRUE. Otherwise it returns FALSE.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._ucxcontrollercreate">UcxControllerCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20UcxControllerNeedsReset method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

