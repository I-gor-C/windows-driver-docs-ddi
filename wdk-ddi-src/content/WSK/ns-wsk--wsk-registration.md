---
UID: NS.wsk._WSK_REGISTRATION
title: WSK_REGISTRATION
author: windows-driver-content
description: The WSK_REGISTRATION structure is used by the WSK subsystem to register or unregister a WSK application as a WSK client.
old-location: netvista\wsk_registration.htm
ms.assetid: 770c53bb-5e11-4bd4-a175-6ea6ae0bb782
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_REGISTRATION
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
ms.keywords: WSK_REGISTRATION, WSK_REGISTRATION, *PWSK_REGISTRATION
req.iface: 
req.product: Windows 10 or later.
---

# WSK_REGISTRATION structure



## -description
<p>The WSK_REGISTRATION structure is used by the WSK subsystem to register or unregister a WSK
  application as a WSK client.</p>


## -syntax

````
typedef struct _WSK_REGISTRATION {
  ULONGLONG  ReservedRegistrationState;
  PVOID      ReservedRegistrationContext;
  KSPIN_LOCK ReservedRegistrationLock;
} WSK_REGISTRATION, *PWSK_REGISTRATION;
````


## -struct-fields
<dl>

### -field <b>ReservedRegistrationState</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <b>ReservedRegistrationContext</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <b>ReservedRegistrationLock</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>
</dl>

## -remarks
<p>This structure is provided by a client application to register or unregister a WSK client instance. Do
    not update any of the members of this structure.</p>

<p>For more information about attaching a WSK application to the WSK subsystem, see 
    <a href="netvista.registering_a_winsock_kernel_application">Registering a Winsock Kernel
    Application</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
</table>