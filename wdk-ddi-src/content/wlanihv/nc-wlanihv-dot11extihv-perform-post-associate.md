---
UID: NC.wlanihv.DOT11EXTIHV_PERFORM_POST_ASSOCIATE
title: DOT11EXTIHV_PERFORM_POST_ASSOCIATE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvperformpostassociate.htm
ms.assetid: a6e9af7d-4c33-4dea-92fe-e2cd8eed6697
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Wlanihv.h, Windot11.h, L2cmn.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvPerformPostAssociate
req.alt-loc: wlanihv.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PrintPropertyValue, PrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_PERFORM_POST_ASSOCIATE callback



## -description

## -prototype

````
DOT11EXTIHV_PERFORM_POST_ASSOCIATE Dot11ExtIhvPerformPostAssociate;

DWORD APIENTRY Dot11ExtIhvPerformPostAssociate(
  _In_opt_ HANDLE                                   hIhvExtAdapter,
  _In_opt_ HANDLE                                   hSecuritySessionID,
  _In_     PDOT11_PORT_STATE                        pPortState,
  _In_     ULONG                                    uDot11AssocParamsBytes,
  _In_     PDOT11_ASSOCIATION_COMPLETION_PARAMETERS pDot11AssocParams
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the wireless LAN (WLAN) adapter. This
     handle value was specified through a previous call to the 
     <a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>hSecuritySessionID</i> [in, optional]

<dd>
<p>The handle of the security session. The IHV Extensions DLL must use this handle value when it
     calls 
     <a href="https://msdn.microsoft.com/25db270c-3de8-4ced-82f1-2cd778006538">
     Dot11ExtPostAssociateCompletion</a> to asynchronously complete the post-association operation.</p>
</dd>

### -param <i>pPortState</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff548753">DOT11_PORT_STATE</a> structure, which
     specifies the current port state of the security session.</p>
</dd>

### -param <i>uDot11AssocParamsBytes</i> [in]

<dd>
<p>The length, in bytes, of the data referenced through the 
     <i>pDot11AssocParams</i> parameter.</p>
</dd>

### -param <i>pDot11AssocParams</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/770962e3-0339-46f8-a789-7c9bbf9e058f">
     DOT11_ASSOCIATION_COMPLETION_PARAMETERS</a> structure, which specifies the result of the association
     operation completed by the WLAN adapter. The Native 802.11 miniport driver, which manages the WLAN
     adapter, includes a DOT11_ASSOCIATION_COMPLETION_PARAMETERS structure when it makes a media-specific 
     <a href="netvista.ndis_status_dot11_association_completion">
     NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION</a> indication.
     </p>
<p>For more information about the association operation, see 
     <a href="NULL">Association Operations</a>.</p>
</dd>
</dl>

## -returns
<p>If the IHV Extension DLL can initiate the post-association operation, it must complete the operation
      asynchronously. In this situation, the function returns ERROR_SUCCESS.</p>

<p>If the IHV Extensions DLL cannot initiate the post-association operation, it returns an error code
      defined in 
      <i>Winerror.h</i>.</p>

## -remarks
<p>The operating system calls the 
    <i>Dot11ExtIhvPerformPostAssociate</i> function to initiate a post-association operation with the IHV
    Extensions DLL. The operating system initiates this operation after the WLAN adapter completes an
    association operation with an access point (AP) in an infrastructure basic service set (BSS) network.</p>

<p>For more information about the association operation, see 
    <a href="NULL">Association Operations</a>.</p>

<p>The post-association operation must be completed asynchronously from the call to 
    <i>Dot11ExtIhvPerformPostAssociate</i>. After the post-association operation completes, the DLL must call
    
    <a href="https://msdn.microsoft.com/25db270c-3de8-4ced-82f1-2cd778006538">
    Dot11ExtPostAssociateCompletion</a>.</p>

<p>If the IHV Extensions DLL can initiate the post-association operation, the 
    <i>Dot11ExtIhvPerformPostAssociate</i> function must return ERROR_SUCCESS and complete the operation
    asynchronously.</p>

<p>For more information about the post-association operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

<p>The operating system calls the 
    <i>Dot11ExtIhvPerformPostAssociate</i> function to initiate a post-association operation with the IHV
    Extensions DLL. The operating system initiates this operation after the WLAN adapter completes an
    association operation with an access point (AP) in an infrastructure basic service set (BSS) network.</p>

<p>For more information about the association operation, see 
    <a href="NULL">Association Operations</a>.</p>

<p>The post-association operation must be completed asynchronously from the call to 
    <i>Dot11ExtIhvPerformPostAssociate</i>. After the post-association operation completes, the DLL must call
    
    <a href="https://msdn.microsoft.com/25db270c-3de8-4ced-82f1-2cd778006538">
    Dot11ExtPostAssociateCompletion</a>.</p>

<p>If the IHV Extensions DLL can initiate the post-association operation, the 
    <i>Dot11ExtIhvPerformPostAssociate</i> function must return ERROR_SUCCESS and complete the operation
    asynchronously.</p>

<p>For more information about the post-association operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

## -requirements
<table>
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
<dt>Wlanihv.h (include Wlanihv.h, Windot11.h, or L2cmn.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548753">DOT11_PORT_STATE</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_association_completion">
   NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c1e8cce7-6fa4-45d3-a8c8-9f2ef0a8e846">Dot11ExtIhvAdapterReset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/96dc1718-ee35-440a-94e8-eba4a41c9559">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/25db270c-3de8-4ced-82f1-2cd778006538">
   Dot11ExtPostAssociateCompletion</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_PERFORM_POST_ASSOCIATE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
