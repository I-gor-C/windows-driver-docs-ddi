---
UID: NS.wlanihv._DOT11EXT_APIS
title: DOT11EXT_APIS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_apis.htm
old-project: netvista
ms.assetid: d533acbb-eb3b-4c49-a057-9a99faaacfc1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11EXT_APIS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_APIS
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

# DOT11EXT_APIS structure



## -description

## -syntax

````
typedef struct _DOT11EXT_APIS {
  DOT11EXT_ALLOCATE_BUFFER                Dot11ExtAllocateBuffer;
  DOT11EXT_FREE_BUFFER                    Dot11ExtFreeBuffer;
  DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA   Dot11ExtSetProfileCustomUserData;
  DOT11EXT_GET_PROFILE_CUSTOM_USER_DATA   Dot11ExtGetProfileCustomUserData;
  DOT11EXT_SET_CURRENT_PROFILE            Dot11ExtSetCurrentProfile;
  DOT11EXT_SEND_UI_REQUEST                Dot11ExtSendUIRequest;
  DOT11EXT_PRE_ASSOCIATE_COMPLETION       Dot11ExtPreAssociateCompletion;
  DOT11EXT_POST_ASSOCIATE_COMPLETION      Dot11ExtPostAssociateCompletion;
  DOT11EXT_SEND_NOTIFICATION              Dot11ExtSendNotification;
  DOT11EXT_SEND_PACKET                    Dot11ExtSendPacket;
  DOT11EXT_SET_ETHERTYPE_HANDLING         Dot11ExtSetEtherTypeHandling;
  DOT11EXT_SET_AUTH_ALGORITHM             Dot11ExtSetAuthAlgorithm;
  DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM   Dot11ExtSetUnicastCipherAlgorithm;
  DOT11EXT_SET_MULTICAST_CIPHER_ALGORITHM Dot11ExtSetMulticastCipherAlgorithm;
  DOT11EXT_SET_DEFAULT_KEY                Dot11ExtSetDefaultKey;
  DOT11EXT_SET_KEY_MAPPING_KEY            Dot11ExtSetKeyMappingKey;
  DOT11EXT_SET_DEFAULT_KEY_ID             Dot11ExtSetDefaultKeyId;
  DOT11EXT_NIC_SPECIFIC_EXTENSION         Dot11ExtNicSpecificExtension;
  DOT11EXT_SET_EXCLUDE_UNENCRYPTED        Dot11ExtSetExcludeUnencrypted;
  DOT11EXT_ONEX_START                     Dot11ExtStartOneX;
  DOT11EXT_ONEX_STOP                      Dot11ExtStopOneX;
  DOT11EXT_PROCESS_ONEX_PACKET            Dot11ExtProcessOneXPacket;
} DOT11EXT_APIS, *PDOT11EXT_APIS;
````


## -struct-fields
<dl>

### -field <b>Dot11ExtAllocateBuffer</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-allocate-buffer.md">
     Dot11ExtAllocateBuffer</a> function.</p>
</dd>

### -field <b>Dot11ExtFreeBuffer</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a> function.</p>
</dd>

### -field <b>Dot11ExtSetProfileCustomUserData</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-profile-custom-user-data.md">
     Dot11ExtSetProfileCustomUserData</a> function.</p>
</dd>

### -field <b>Dot11ExtGetProfileCustomUserData</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-get-profile-custom-user-data.md">
     Dot11ExtGetProfileCustomUserData</a> function.</p>
</dd>

### -field <b>Dot11ExtSetCurrentProfile</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-current-profile.md">
     Dot11ExtSetCurrentProfile</a> function.</p>
</dd>

### -field <b>Dot11ExtSendUIRequest</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-send-ui-request.md">
     Dot11ExtSendUIRequest</a> function.</p>
</dd>

### -field <b>Dot11ExtPreAssociateCompletion</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-pre-associate-completion.md">
     Dot11ExtPreAssociateCompletion</a> function.</p>
</dd>

### -field <b>Dot11ExtPostAssociateCompletion</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
     Dot11ExtPostAssociateCompletion</a> function.</p>
</dd>

### -field <b>Dot11ExtSendNotification</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-send-notification.md">
     Dot11ExtSendNotification</a> function.</p>
</dd>

### -field <b>Dot11ExtSendPacket</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-send-packet.md">Dot11ExtSendPacket</a> function.</p>
</dd>

### -field <b>Dot11ExtSetEtherTypeHandling</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-ethertype-handling.md">
     Dot11ExtSetEtherTypeHandling</a> function.</p>
</dd>

### -field <b>Dot11ExtSetAuthAlgorithm</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-auth-algorithm.md">
     Dot11ExtSetAuthAlgorithm</a> function.</p>
</dd>

### -field <b>Dot11ExtSetUnicastCipherAlgorithm</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-unicast-cipher-algorithm.md">
     Dot11ExtSetUnicastCipherAlgorithm</a> function.</p>
</dd>

### -field <b>Dot11ExtSetMulticastCipherAlgorithm</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-multicast-cipher-algorithm.md">
     Dot11ExtSetMulticastCipherAlgorithm</a> function.</p>
</dd>

### -field <b>Dot11ExtSetDefaultKey</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-default-key.md">
     Dot11ExtSetDefaultKey</a> function.</p>
</dd>

### -field <b>Dot11ExtSetKeyMappingKey</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-key-mapping-key.md">
     Dot11ExtSetKeyMappingKey</a> function.</p>
</dd>

### -field <b>Dot11ExtSetDefaultKeyId</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-default-key-id.md">
     Dot11ExtSetDefaultKeyId</a> function.</p>
</dd>

### -field <b>Dot11ExtNicSpecificExtension</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-nic-specific-extension.md">
     Dot11ExtNicSpecificExtension</a> function.</p>
</dd>

### -field <b>Dot11ExtSetExcludeUnencrypted</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-set-exclude-unencrypted.md">
     Dot11ExtSetExcludeUnencrypted</a> function.</p>
</dd>

### -field <b>Dot11ExtStartOneX</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a> function.</p>
</dd>

### -field <b>Dot11ExtStopOneX</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-onex-stop.md">Dot11ExtStopOneX</a> function.</p>
</dd>

### -field <b>Dot11ExtProcessOneXPacket</b>

<dd>
<p>A pointer to the 
     <a href="..\wlanihv\nc-wlanihv-dot11ext-process-onex-packet.md">
     Dot11ExtProcessOneXPacket</a> function.</p>
</dd>
</dl>

## -remarks
<p>The IHV Extensibility functions are not statically or dynamically linked to the IHV Extensions DLL.
    Instead, when the operating system calls the 
    <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a> IHV
    handler function, it passes the list of pointers to the IHV Extensibility functions through the 
    <i>pDot11ExtAPI</i> parameter.</p>

<p>All of the function pointers are required and will not be set to <b>NULL</b>.</p>

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
<a href="..\wlanihv\nc-wlanihv-dot11ext-get-profile-custom-user-data.md">Dot11ExtGetUserData</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-service.md">Dot11ExtIhvInitService</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-nic-specific-extension.md">Dot11ExtNicSpecificExtension</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-onex-start.md">Dot11ExtStartOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-onex-stop.md">Dot11ExtStopOneX</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
   Dot11ExtPostAssociateCompletion</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-pre-associate-completion.md">
   Dot11ExtPreAssociateCompletion</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-process-onex-packet.md">Dot11ExtProcessOneXPacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-send-notification.md">Dot11ExtSendNotification</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-send-packet.md">Dot11ExtSendPacket</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-send-ui-request.md">Dot11ExtSendUIRequest</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-auth-algorithm.md">Dot11ExtSetAuthAlgorithm</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-current-profile.md">Dot11ExtSetCurrentProfile</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-default-key.md">Dot11ExtSetDefaultKey</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-default-key-id.md">Dot11ExtSetDefaultKeyId</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-ethertype-handling.md">Dot11ExtSetEtherTypeHandling</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-exclude-unencrypted.md">
   Dot11ExtSetExcludeUnencrypted</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-key-mapping-key.md">Dot11ExtSetKeyMappingKey</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-multicast-cipher-algorithm.md">
   Dot11ExtSetMulticastCipherAlgorithm</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-profile-custom-user-data.md">
   Dot11ExtSetProfileCustomUserData</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-set-unicast-cipher-algorithm.md">
   Dot11ExtSetUnicastCipherAlgorithm</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_extensibility_functions">Native 802.11 IHV
   Extensibility Functions</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_APIS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
