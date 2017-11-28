---
UID: NE.rilapitypes.RILNOTIFICATIONS
title: RILNOTIFICATIONS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnotifications_2.htm
old-project: netvista
ms.assetid: 90a46631-b365-46ee-8c66-085ec8d55f57
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILNOTIFICATIONS
req.alt-loc: rilapitypes.h
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

# RILNOTIFICATIONS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILNOTIFICATIONS { 
  RIL_NOTIFY_RADIOEQUIPMENTSTATECHANGED,
  RIL_NOTIFY_RADIOPRESENCECHANGED,
  RIL_NOTIFY_UICCFILE_DATACHANGE,
  RIL_NOTIFY_UICCAPP_DATACHANGE,
  RIL_NOTIFY_SLOTINFOCHANGED,
  RIL_NOTIFY_CARDAPPREMOVED,
  RIL_NOTIFY_CARDAPPADDED,
  RIL_NOTIFY_UICCLOCKSTATUS,
  RIL_NOTIFY_UICCAPPPERSOCHECKSTATUS,
  RIL_NOTIFY_PHONEBOOKENTRYDELETED,
  RIL_NOTIFY_PHONEBOOKENTRYSTORED,
  RIL_NOTIFY_PHONEBOOKREADYSTATE,
  RIL_NOTIFY_EMERGENCYNUMBERLISTCHANGED,
  RIL_NOTIFY_REGSTATUSCHANGED,
  RIL_NOTIFY_LOCATIONUPDATE,
  RIL_NOTIFY_NETWORKCODECHANGED,
  RIL_NOTIFY_PROVISION_STATUS,
  RIL_NOTIFY_SYSTEMPREFSCHANGED,
  RIL_NOTIFY_EXECUTORSTATE,
  RIL_NOTIFY_MANAGED_ROAMING,
  RIL_NOTIFY_SIGNALQUALITY,
  RIL_NOTIFY_NITZ,
  RIL_NOTIFY_UICCTOOLKITCMD,
  RIL_NOTIFY_CALLMODIFICATIONINFO,
  RIL_NOTIFY_CALLPROGRESSINFO,
  RIL_NOTIFY_EMERGENCYMODEENTERED,
  RIL_NOTIFY_EMERGENCYMODEEXITED,
  RIL_NOTIFY_CALLWAITING,
  RIL_NOTIFY_DIALEDID,
  RIL_NOTIFY_DISPLAY,
  RIL_NOTIFY_SUPSVCINFO,
  RIL_NOTIFY_SUPSERVICEDATA,
  RIL_NOTIFY_UNSOLICITEDSS,
  RIL_NOTIFY_LINECONTROL,
  RIL_NOTIFY_MESSAGE,
  RIL_NOTIFY_MESSAGE_IN_UICC,
  RIL_NOTIFY_IMSSTATUS,
  RIL_NOTIFY_ADDITIONALNUMBERSTRINGUPDATED,
  RIL_NOTIFY_SUPSERVICEDATATERMINATED,
  RIL_NOTIFY_CLEARIDLEMODETEXT,
  RIL_NOTIFY_MESSAGE_STORAGE_FULL,
  RIL_NOTIFY_TONESIGNAL,
  RIL_NOTIFY_FORWARDSTARTDTMF,
  RIL_NOTIFY_FORWARDSTOPDTMF,
  RIL_NOTIFY_FORWARDBURSTDTMF,
  RIL_NOTIFY_EXECUTORFOCUSSTATECHANGED,
  RIL_NOTIFY_EXECUTORRFSTATE,
  RIL_NOTIFY_MODEMRESET,
  RIL_NOTIFY_RADIOCONFIGURATION,
  RIL_NOTIFY_IMSHANDOVERATTEMPT,
  RIL_NOTIFY_ADDITIONALCALLERINFO,
  RIL_NOTIFY_MWISUMMARY,
  RIL_NOTIFY_MWIDETAILS,
  RIL_NOTIFY_IMSFAILURE,
  RIL_NOTIFY_CONFPARTICIPANTSTATUS,
  RIL_NOTIFY_SMSREADYSTATUS,
  RIL_NOTIFY_REQUESTGEOLOCATIONDATA,
  RIL_NOTIFY_RTT,
  RIL_NOTIFY_COUNT
} RILNOTIFICATIONS;
````


## -enum-fields
<dl>

### -field <a id="RIL_NOTIFY_RADIOEQUIPMENTSTATECHANGED"></a><a id="ril_notify_radioequipmentstatechanged"></a><b>RIL_NOTIFY_RADIOEQUIPMENTSTATECHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_RADIOPRESENCECHANGED"></a><a id="ril_notify_radiopresencechanged"></a><b>RIL_NOTIFY_RADIOPRESENCECHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UICCFILE_DATACHANGE"></a><a id="ril_notify_uiccfile_datachange"></a><b>RIL_NOTIFY_UICCFILE_DATACHANGE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UICCAPP_DATACHANGE"></a><a id="ril_notify_uiccapp_datachange"></a><b>RIL_NOTIFY_UICCAPP_DATACHANGE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SLOTINFOCHANGED"></a><a id="ril_notify_slotinfochanged"></a><b>RIL_NOTIFY_SLOTINFOCHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CARDAPPREMOVED"></a><a id="ril_notify_cardappremoved"></a><b>RIL_NOTIFY_CARDAPPREMOVED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CARDAPPADDED"></a><a id="ril_notify_cardappadded"></a><b>RIL_NOTIFY_CARDAPPADDED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UICCLOCKSTATUS"></a><a id="ril_notify_uicclockstatus"></a><b>RIL_NOTIFY_UICCLOCKSTATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UICCAPPPERSOCHECKSTATUS"></a><a id="ril_notify_uiccapppersocheckstatus"></a><b>RIL_NOTIFY_UICCAPPPERSOCHECKSTATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_PHONEBOOKENTRYDELETED"></a><a id="ril_notify_phonebookentrydeleted"></a><b>RIL_NOTIFY_PHONEBOOKENTRYDELETED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_PHONEBOOKENTRYSTORED"></a><a id="ril_notify_phonebookentrystored"></a><b>RIL_NOTIFY_PHONEBOOKENTRYSTORED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_PHONEBOOKREADYSTATE"></a><a id="ril_notify_phonebookreadystate"></a><b>RIL_NOTIFY_PHONEBOOKREADYSTATE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EMERGENCYNUMBERLISTCHANGED"></a><a id="ril_notify_emergencynumberlistchanged"></a><b>RIL_NOTIFY_EMERGENCYNUMBERLISTCHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_REGSTATUSCHANGED"></a><a id="ril_notify_regstatuschanged"></a><b>RIL_NOTIFY_REGSTATUSCHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_LOCATIONUPDATE"></a><a id="ril_notify_locationupdate"></a><b>RIL_NOTIFY_LOCATIONUPDATE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_NETWORKCODECHANGED"></a><a id="ril_notify_networkcodechanged"></a><b>RIL_NOTIFY_NETWORKCODECHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_PROVISION_STATUS"></a><a id="ril_notify_provision_status"></a><b>RIL_NOTIFY_PROVISION_STATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SYSTEMPREFSCHANGED"></a><a id="ril_notify_systemprefschanged"></a><b>RIL_NOTIFY_SYSTEMPREFSCHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EXECUTORSTATE"></a><a id="ril_notify_executorstate"></a><b>RIL_NOTIFY_EXECUTORSTATE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MANAGED_ROAMING"></a><a id="ril_notify_managed_roaming"></a><b>RIL_NOTIFY_MANAGED_ROAMING</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SIGNALQUALITY"></a><a id="ril_notify_signalquality"></a><b>RIL_NOTIFY_SIGNALQUALITY</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_NITZ"></a><a id="ril_notify_nitz"></a><b>RIL_NOTIFY_NITZ</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UICCTOOLKITCMD"></a><a id="ril_notify_uicctoolkitcmd"></a><b>RIL_NOTIFY_UICCTOOLKITCMD</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CALLMODIFICATIONINFO"></a><a id="ril_notify_callmodificationinfo"></a><b>RIL_NOTIFY_CALLMODIFICATIONINFO</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CALLPROGRESSINFO"></a><a id="ril_notify_callprogressinfo"></a><b>RIL_NOTIFY_CALLPROGRESSINFO</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EMERGENCYMODEENTERED"></a><a id="ril_notify_emergencymodeentered"></a><b>RIL_NOTIFY_EMERGENCYMODEENTERED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EMERGENCYMODEEXITED"></a><a id="ril_notify_emergencymodeexited"></a><b>RIL_NOTIFY_EMERGENCYMODEEXITED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CALLWAITING"></a><a id="ril_notify_callwaiting"></a><b>RIL_NOTIFY_CALLWAITING</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_DIALEDID"></a><a id="ril_notify_dialedid"></a><b>RIL_NOTIFY_DIALEDID</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_DISPLAY"></a><a id="ril_notify_display"></a><b>RIL_NOTIFY_DISPLAY</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SUPSVCINFO"></a><a id="ril_notify_supsvcinfo"></a><b>RIL_NOTIFY_SUPSVCINFO</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SUPSERVICEDATA"></a><a id="ril_notify_supservicedata"></a><b>RIL_NOTIFY_SUPSERVICEDATA</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_UNSOLICITEDSS"></a><a id="ril_notify_unsolicitedss"></a><b>RIL_NOTIFY_UNSOLICITEDSS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_LINECONTROL"></a><a id="ril_notify_linecontrol"></a><b>RIL_NOTIFY_LINECONTROL</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MESSAGE"></a><a id="ril_notify_message"></a><b>RIL_NOTIFY_MESSAGE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MESSAGE_IN_UICC"></a><a id="ril_notify_message_in_uicc"></a><b>RIL_NOTIFY_MESSAGE_IN_UICC</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_IMSSTATUS"></a><a id="ril_notify_imsstatus"></a><b>RIL_NOTIFY_IMSSTATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_ADDITIONALNUMBERSTRINGUPDATED"></a><a id="ril_notify_additionalnumberstringupdated"></a><b>RIL_NOTIFY_ADDITIONALNUMBERSTRINGUPDATED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SUPSERVICEDATATERMINATED"></a><a id="ril_notify_supservicedataterminated"></a><b>RIL_NOTIFY_SUPSERVICEDATATERMINATED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CLEARIDLEMODETEXT"></a><a id="ril_notify_clearidlemodetext"></a><b>RIL_NOTIFY_CLEARIDLEMODETEXT</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MESSAGE_STORAGE_FULL"></a><a id="ril_notify_message_storage_full"></a><b>RIL_NOTIFY_MESSAGE_STORAGE_FULL</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_TONESIGNAL"></a><a id="ril_notify_tonesignal"></a><b>RIL_NOTIFY_TONESIGNAL</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_FORWARDSTARTDTMF"></a><a id="ril_notify_forwardstartdtmf"></a><b>RIL_NOTIFY_FORWARDSTARTDTMF</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_FORWARDSTOPDTMF"></a><a id="ril_notify_forwardstopdtmf"></a><b>RIL_NOTIFY_FORWARDSTOPDTMF</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_FORWARDBURSTDTMF"></a><a id="ril_notify_forwardburstdtmf"></a><b>RIL_NOTIFY_FORWARDBURSTDTMF</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EXECUTORFOCUSSTATECHANGED"></a><a id="ril_notify_executorfocusstatechanged"></a><b>RIL_NOTIFY_EXECUTORFOCUSSTATECHANGED</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_EXECUTORRFSTATE"></a><a id="ril_notify_executorrfstate"></a><b>RIL_NOTIFY_EXECUTORRFSTATE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MODEMRESET"></a><a id="ril_notify_modemreset"></a><b>RIL_NOTIFY_MODEMRESET</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_RADIOCONFIGURATION"></a><a id="ril_notify_radioconfiguration"></a><b>RIL_NOTIFY_RADIOCONFIGURATION</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_IMSHANDOVERATTEMPT"></a><a id="ril_notify_imshandoverattempt"></a><b>RIL_NOTIFY_IMSHANDOVERATTEMPT</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_ADDITIONALCALLERINFO"></a><a id="ril_notify_additionalcallerinfo"></a><b>RIL_NOTIFY_ADDITIONALCALLERINFO</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MWISUMMARY"></a><a id="ril_notify_mwisummary"></a><b>RIL_NOTIFY_MWISUMMARY</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_MWIDETAILS"></a><a id="ril_notify_mwidetails"></a><b>RIL_NOTIFY_MWIDETAILS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_IMSFAILURE"></a><a id="ril_notify_imsfailure"></a><b>RIL_NOTIFY_IMSFAILURE</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_CONFPARTICIPANTSTATUS"></a><a id="ril_notify_confparticipantstatus"></a><b>RIL_NOTIFY_CONFPARTICIPANTSTATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_SMSREADYSTATUS"></a><a id="ril_notify_smsreadystatus"></a><b>RIL_NOTIFY_SMSREADYSTATUS</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_REQUESTGEOLOCATIONDATA"></a><a id="ril_notify_requestgeolocationdata"></a><b>RIL_NOTIFY_REQUESTGEOLOCATIONDATA</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_RTT"></a><a id="ril_notify_rtt"></a><b>RIL_NOTIFY_RTT</b>

<dd></dd>

### -field <a id="RIL_NOTIFY_COUNT"></a><a id="ril_notify_count"></a><b>RIL_NOTIFY_COUNT</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>