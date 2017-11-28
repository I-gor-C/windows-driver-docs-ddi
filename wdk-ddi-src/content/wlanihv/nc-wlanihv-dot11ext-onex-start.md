---
UID: NC.wlanihv.DOT11EXT_ONEX_START
title: DOT11EXT_ONEX_START
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extstartonex.htm
old-project: netvista
ms.assetid: d4117da4-349a-4143-b2a8-d4edf6c02e7b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtStartOneX
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

# DOT11EXT_ONEX_START callback



## -description

## -prototype

````
DWORD WINAPI * Dot11ExtStartOneX(
  _In_opt_ HANDLE         hDot11SvcHandle,
  _In_opt_ EAP_ATTRIBUTES *pEapAttribute
);
````


## -parameters
<dl>

### -param <i>hDot11SvcHandle</i> [in, optional]

<dd>
<p>The handle used by the operating system to reference the wireless LAN (WLAN) adapter. This handle
     value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param <i>pEapAttribute</i> [in, optional]

<dd>
<p>A pointer to an EAP_ATTRIBUTES array structure that contains the EAP attributes returned by the
     authentication session. For more information about EAP_ATTRIBUTES, see the Microsoft Windows SDK
     documentation.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>The IHV Extensions DLL can initiate an 802.1X authentication operation by using the 802.1X module of
    the Native 802.11 framework. This allows the DLL to use the standard extensible authentication protocol
    (EAP) algorithms that are supported by the operating system.</p>

<p>The IHV Extensions DLL initiates the 802.1X authentication operation by calling the 
    <b>Dot11ExtStartOneX</b> function. 
    <b>Dot11ExtStartOneX</b> can only be called either during a post-association
    operation or after the operation has completed. For more information about this operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

<p>When the 
    <b>Dot11ExtStartOneX</b> function is called, the operating system sends an EAP
    over LAN (EAPOL) Start packet to the AP. If the AP fails to respond after three transmissions of the
    EAPOL-Start packet, the operating system fails the 802.1X authentication operation and calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
    Dot11ExtIhvOneXIndicateResult</a> IHV Handler function. For more information about the EAPOL-Start
    packet, refer to Clause 7.5 and Clause 8.4.2 of the IEEE 802.1X-1999 standard.</p>

<p>After the 802.1X authentication operation is initiated, the IHV Extensions DLL must follow these
    guidelines.</p>

<p>The IHV Extensions must forward all EAPOL packets to the operating system for processing. When the
      DLL receives an EAPOL packet through a call to the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a> IHV
      Handler function, the DLL must call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547541">Dot11ExtProcessOneXPacket</a> to
      forward the packet to the operating system.</p>

<p>For more information about EAPOL packets, refer to Clause 7 of the IEEE 802.1X-2001 standard.</p>

<p>When the 802.1X authentication operation is completed, the operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
      Dot11ExtIhvOneXIndicateResult</a> IHV Handler function to indicate that authorization is in
      progress.</p>

<p>The IHV Extensions DLL can cancel the 802.1X authentication operation by calling 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547614">Dot11ExtStopOneX</a>.</p>

<p>For more information about using the 802.1X module for authentication, see 
    <a href="netvista.interface_to_the_native_802_11_802_1x_module">Interface to the Native
    802.11 802.1X Module</a>.</p>

<p>The IHV Extensions DLL can initiate an 802.1X authentication operation by using the 802.1X module of
    the Native 802.11 framework. This allows the DLL to use the standard extensible authentication protocol
    (EAP) algorithms that are supported by the operating system.</p>

<p>The IHV Extensions DLL initiates the 802.1X authentication operation by calling the 
    <b>Dot11ExtStartOneX</b> function. 
    <b>Dot11ExtStartOneX</b> can only be called either during a post-association
    operation or after the operation has completed. For more information about this operation, see 
    <a href="NULL">Post-Association Operations</a>.</p>

<p>When the 
    <b>Dot11ExtStartOneX</b> function is called, the operating system sends an EAP
    over LAN (EAPOL) Start packet to the AP. If the AP fails to respond after three transmissions of the
    EAPOL-Start packet, the operating system fails the 802.1X authentication operation and calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
    Dot11ExtIhvOneXIndicateResult</a> IHV Handler function. For more information about the EAPOL-Start
    packet, refer to Clause 7.5 and Clause 8.4.2 of the IEEE 802.1X-1999 standard.</p>

<p>After the 802.1X authentication operation is initiated, the IHV Extensions DLL must follow these
    guidelines.</p>

<p>The IHV Extensions must forward all EAPOL packets to the operating system for processing. When the
      DLL receives an EAPOL packet through a call to the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a> IHV
      Handler function, the DLL must call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547541">Dot11ExtProcessOneXPacket</a> to
      forward the packet to the operating system.</p>

<p>For more information about EAPOL packets, refer to Clause 7 of the IEEE 802.1X-2001 standard.</p>

<p>When the 802.1X authentication operation is completed, the operating system calls the 
      <a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
      Dot11ExtIhvOneXIndicateResult</a> IHV Handler function to indicate that authorization is in
      progress.</p>

<p>The IHV Extensions DLL can cancel the 802.1X authentication operation by calling 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547614">Dot11ExtStopOneX</a>.</p>

<p>For more information about using the 802.1X module for authentication, see 
    <a href="netvista.interface_to_the_native_802_11_802_1x_module">Interface to the Native
    802.11 802.1X Module</a>.</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-onex-indicate-result.md">
   Dot11ExtIhvOneXIndicateResult</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-post-associate.md">
   Dot11ExtIhvPerformPostAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-receive-packet.md">Dot11ExtIhvReceivePacket</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547614">Dot11ExtStopOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
   Dot11ExtPostAssociateCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547541">Dot11ExtProcessOneXPacket</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_ONEX_START callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
