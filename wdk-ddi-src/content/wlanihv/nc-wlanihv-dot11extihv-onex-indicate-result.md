---
UID: NC.wlanihv.DOT11EXTIHV_ONEX_INDICATE_RESULT
title: DOT11EXTIHV_ONEX_INDICATE_RESULT
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvonexindicateresult.htm
old-project: netvista
ms.assetid: bf865b33-6e44-4724-868d-73150cf5b589
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
req.alt-api: Dot11ExtIhvOneXIndicateResult
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

# DOT11EXTIHV_ONEX_INDICATE_RESULT callback



## -description

## -prototype

````
DOT11EXTIHV_ONEX_INDICATE_RESULT Dot11ExtIhvOneXIndicateResult;

DWORD APIENTRY Dot11ExtIhvOneXIndicateResult(
  _In_opt_ HANDLE                      hIhvExtAdapter,
  _In_     DOT11_MSONEX_RESULT         msOneXResult,
  _In_opt_ PDOT11_MSONEX_RESULT_PARAMS pDot11MsOneXResultParams
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

### -param <i>msOneXResult</i> [in]

<dd>
<p>The result of the 802.1X authentication operation specified through a 
     <a href="..\wlanihv\ne-wlanihv--dot11-msonex-result.md">DOT11_MSONEX_RESULT</a> enumeration
     value.</p>
</dd>

### -param <i>pDot11MsOneXResultParams</i> [in, optional]

<dd>
<p>A pointer to a 
     <a href="..\wlanihv\ns-wlanihv--dot11-msonex-result-params.md">
     DOT11_MSONEX_RESULT_PARAMS</a> structure that contains result parameters.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The IHV Extensions DLL can initiate an 802.1X authentication operation by using the 802.1X module of
    the Native 802.11 framework. This allows the DLL to make use of the standard extensible authentication
    protocol (EAP) algorithms that are supported by the operating system.</p>

<p>The IHV Extensions DLL initiates the 802.1X authentication operation by calling the 
    <a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a> function. 
    <b>Dot11ExtStartOneX</b> can only be called either during a post-association operation or after the
    operation has completed. For more information about this operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

<p>After the operating system has completed the 802.1X authentication operation, it calls the 
    <i>
    Dot11ExtIhvOneXIndicateResult</i> IHV Handler function.</p>

<p>For more information about using the 802.1X module for authentication, see 
    <a href="netvista.interface_to_the_native_802_11_802_1x_module">Interface to the Native
    802.11 802.1X Module</a>
</p>

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
<a href="..\wlanihv\ne-wlanihv--dot11-msonex-result.md">DOT11_MSONEX_RESULT</a>
</dt>
<dt>
<a href="..\wlanihv\ns-wlanihv--dot11-msonex-result-params.md">DOT11_MSONEX_RESULT_PARAMS</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
   Dot11ExtIhvOneXIndicateResult</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-process-onex-packet.md">Dot11ExtProcessOneXPacket</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_ONEX_INDICATE_RESULT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
