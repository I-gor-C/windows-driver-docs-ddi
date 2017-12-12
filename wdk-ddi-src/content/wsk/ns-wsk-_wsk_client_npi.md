---
UID: NS.WSK._WSK_CLIENT_NPI
title: _WSK_CLIENT_NPI
author: windows-driver-content
description: The WSK_CLIENT_NPI structure identifies a Network Programming Interface (NPI) implemented by a WSK client.
old-location: netvista\wsk_client_npi.htm
old-project: netvista
ms.assetid: 2f50b228-5565-436f-8c68-8885b8916001
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WSK_CLIENT_NPI, *PWSK_CLIENT_NPI, WSK_CLIENT_NPI
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_CLIENT_NPI
req.alt-loc: wsk.h
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
req.product: Windows 10 or later.
---

# _WSK_CLIENT_NPI structure



## -description
The WSK_CLIENT_NPI structure identifies a 
  <a href="netvista.network_programming_interface">Network Programming Interface
  (NPI)</a> implemented by a WSK client.



## -syntax

````
typedef struct _WSK_CLIENT_NPI {
  PVOID                     ClientContext;
  const WSK_CLIENT_DISPATCH *Dispatch;
} WSK_CLIENT_NPI, *PWSK_CLIENT_NPI;
````


## -struct-fields

### -field ClientContext

A pointer to the context for the WSK application's binding to the WSK subsystem.


### -field Dispatch

A pointer to a constant 
     <a href="netvista.wsk_client_dispatch">WSK_CLIENT_DISPATCH</a> structure.


## -remarks
For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating
   systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.wsk_client_dispatch">WSK_CLIENT_DISPATCH</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_CLIENT_NPI structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

