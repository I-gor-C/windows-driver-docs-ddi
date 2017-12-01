---
UID: NC.wlanihv.DOT11EXTIHV_QUERY_UI_REQUEST
title: DOT11EXTIHV_QUERY_UI_REQUEST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvqueryuirequest.htm
old-project: netvista
ms.assetid: 37c01180-0742-4764-88c3-9ceb807a0086
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvQueryUIRequest
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11EXTIHV_QUERY_UI_REQUEST callback



## -description

## -prototype

````
DOT11EXTIHV_QUERY_UI_REQUEST Dot11ExtIhvQueryUIRequest;

DWORD APIENTRY Dot11ExtIhvQueryUIRequest(
  _In_opt_ HANDLE                        hIhvExtAdapter,
  _In_     DOT11EXT_IHV_CONNECTION_PHASE connectionPhase,
  _Out_    PDOT11EXT_IHV_UI_REQUEST      *ppIhvUIRequest
)
{ ... }
````


## -parameters
<dl>

### -param <i>hIhvExtAdapter</i> [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the wireless LAN (WLAN) adapter. This
     handle value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>connectionPhase</i> [in]

<dd>
<p>The current connection phase. The data type for this member is the 
     <b>DOT11EXT_IHV_CONNECTION_PHASE</b> enumeration:
     </p>
<p></p>
<dl>

### -param <a id="connection_phase_any"></a><a id="CONNECTION_PHASE_ANY"></a><b>connection_phase_any</b>

<dd>
<p>Specifies any connection phase.</p>
</dd>

### -param <a id="connection_phase_initial_connection"></a><a id="CONNECTION_PHASE_INITIAL_CONNECTION"></a><b>connection_phase_initial_connection</b>

<dd>
<p>Specifies the connection phase before the IHV Extensions DLL initiates a pre-association
       operation. For more information about the pre-association operation, see 
       <a href="netvista.pre_association_operations">Pre-Association
       Operations</a>.</p>
</dd>

### -param <a id="connection_phase_post_l3_connection"></a><a id="CONNECTION_PHASE_POST_L3_CONNECTION"></a><b>connection_phase_post_l3_connection</b>

<dd>
<p>Specifies the connection phase after the IHV Extensions DLL completes a post-association
       operation. For more information about the post-association operation, see 
       <a href="netvista.post_association_operations">Post-Association
       Operations</a>.</p>
</dd>
</dl>
</dd>

### -param <i>ppIhvUIRequest</i> [out]

<dd>
<p>The address of a pointer to a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-ui-request.md">DOT11EXT_IHV_UI_REQUEST</a> structure.
     The IHV Extensions DLL must allocate a buffer for the DOT11EXT_IHV_UI_REQUEST structure by calling 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-allocate-buffer.md">Dot11ExtAllocateBuffer</a>.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>When 
    <i>Dot11ExtIhvQueryUIRequest</i> is called, the IHV Extensions DLL must allocate and return a buffer
    formatted as a 
    <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-ui-request.md">DOT11EXT_IHV_UI_REQUEST</a> structure.
    In this situation, the DLL must follow these guidelines:</p>

<p>The IHV Extensions DLL must call 
      <a href="..\wlanihv\nc-wlanihv-dot11ext-allocate-buffer.md">Dot11ExtAllocateBuffer</a> to
      allocate the buffer. After the DLL returns from 
      <i>Dot11ExtIhvQueryUIRequest</i>, the operating system is responsible for calling 
      <a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a> to free the
      buffer.</p>

<p>The IHV Extensions DLL formats the 
      <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-ui-request.md">DOT11EXT_IHV_UI_REQUEST</a> structure
      for a UI request appropriate for the change in connection status.</p>

<p>For example, if 
      <i>connectionPhase</i> is set to 
      <b>connection_phase_initial_connection</b>, the IHV Extensions DLL could set the members of the
      DOT11EXT_IHV_UI_REQUEST structure to reference a user interface page that notifies the user of the
      start of the connection operation.</p>

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
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-allocate-buffer.md">Dot11ExtAllocateBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-ui-request.md">DOT11EXT_IHV_UI_REQUEST</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_QUERY_UI_REQUEST callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
