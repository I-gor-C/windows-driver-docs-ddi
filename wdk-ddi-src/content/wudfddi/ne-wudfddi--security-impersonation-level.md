---
UID: NE.wudfddi._SECURITY_IMPERSONATION_LEVEL
title: SECURITY_IMPERSONATION_LEVEL
author: windows-driver-content
description: The SECURITY_IMPERSONATION_LEVEL enumeration contains values that identify security impersonation levels.
old-location: wdf\security_impersonation_level.htm
old-project: wdf
ms.assetid: 5c325c16-6bc6-4eae-a58c-234d11616780
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WSK_TRANSPORT, WSK_TRANSPORT, *PWSK_TRANSPORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURITY_IMPERSONATION_LEVEL
req.alt-loc: Wudfddi.h
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
req.iface: 
req.product: Windows 10 or later.
---

# SECURITY_IMPERSONATION_LEVEL enumeration



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>SECURITY_IMPERSONATION_LEVEL</b> enumeration contains values that identify security impersonation levels.</p>


## -syntax

````
typedef enum _SECURITY_IMPERSONATION_LEVEL { 
  SecurityAnonymous       = 0,
  SecurityIdentification  = ( SecurityAnonymous + 1 ),
  SecurityImpersonation   = ( SecurityIdentification + 1 ),
  SecurityDelegation      = ( SecurityImpersonation + 1 )
} SECURITY_IMPERSONATION_LEVEL;
````


## -enum-fields
<dl>

### -field SecurityAnonymous

<dd>
<p>The driver cannot impersonate or identify the client.</p>
</dd>

### -field SecurityIdentification

<dd>
<p>The driver can obtain the identity and privileges of the client but cannot impersonate the client.</p>
</dd>

### -field SecurityImpersonation

<dd>
<p>The driver can impersonate the client's security context on the local system.</p>
</dd>

### -field SecurityDelegation

<dd>
<p>The driver can impersonate the client's security context on remote systems.</p>
</dd>
</dl>

## -remarks
<p>For more information about impersonation in the UMDF, see <a href="wdf.handling_client_impersonation">Handling Client Impersonation</a>.</p>

<p>A UMDF driver supplies one of the values of <b>SECURITY_IMPERSONATION_LEVEL</b> to the <a href="wdf.iwdfiorequest_impersonate">IWDFIoRequest::Impersonate</a> method to set the security impersonation level.</p>

<p>For more information about the security impersonation levels, see the <b>SECURITY_IMPERSONATION_LEVEL</b> enumeration type in the Microsoft Windows SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.iwdfiorequest_impersonate">IWDFIoRequest::Impersonate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20SECURITY_IMPERSONATION_LEVEL enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
