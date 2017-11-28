---
UID: NE.rilapitypes.RILERRORCODES
title: RILERRORCODES
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilerrorcodes_2.htm
old-project: netvista
ms.assetid: 79561e8c-63b9-4afa-9c16-9ab82945da7a
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
req.alt-api: RILERRORCODES
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

# RILERRORCODES enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILERRORCODES { 
  RIL_E_NOCONNECTION,
  RIL_E_LINKRESERVED,
  RIL_E_OPNOTALLOWED,
  RIL_E_OPNOTSUPPORTED,
  RIL_E_UICCNOTINSERTED,
  RIL_E_UICCFAILURE,
  RIL_E_UICCBUSY,
  RIL_E_UICCWRONG,
  RIL_E_INCORRECTPASSWORD,
  RIL_E_MEMORYFULL,
  RIL_E_INVALIDINDEX,
  RIL_E_NOTFOUND,
  RIL_E_MEMORYFAILURE,
  RIL_E_TEXTSTRINGTOOLONG,
  RIL_E_INVALIDTEXTSTRING,
  RIL_E_DIALSTRINGTOOLONG,
  RIL_E_INVALIDDIALSTRING,
  RIL_E_NONETWORKSVC,
  RIL_E_NETWORKTIMEOUT,
  RIL_E_EMERGENCYONLY,
  RIL_E_TELEMATICIWUNSUPPORTED,
  RIL_E_SMTYPE0UNSUPPORTED,
  RIL_E_CANTREPLACEMSG,
  RIL_E_PROTOCOLIDERROR,
  RIL_E_DCSUNSUPPORTED,
  RIL_E_MSGCLASSUNSUPPORTED,
  RIL_E_DCSERROR,
  RIL_E_CMDCANTBEACTIONED,
  RIL_E_CMDUNSUPPORTED,
  RIL_E_CMDERROR,
  RIL_E_MSGBODYHEADERERROR,
  RIL_E_SCBUSY,
  RIL_E_NOSCSUBSCRIPTION,
  RIL_E_SCSYSTEMFAILURE,
  RIL_E_INVALIDADDRESS,
  RIL_E_DESTINATIONBARRED,
  RIL_E_REJECTEDDUPLICATE,
  RIL_E_VPFUNSUPPORTED,
  RIL_E_VPUNSUPPORTED,
  RIL_E_UICCMSGSTORAGEFULL,
  RIL_E_NOUICCMSGSTORAGE,
  RIL_E_UICCTOOLKITBUSY,
  RIL_E_UICCDOWNLOADERROR,
  RIL_E_MSGSVCRESERVED,
  RIL_E_INVALIDMSGPARAM,
  RIL_E_INVALIDSCADDRESS,
  RIL_E_UNASSIGNEDNUMBER,
  RIL_E_MSGBARREDBYOPERATOR,
  RIL_E_MSGCALLBARRED,
  RIL_E_MSGXFERREJECTED,
  RIL_E_DESTINATIONOUTOFSVC,
  RIL_E_UNIDENTIFIEDSUBCRIBER,
  RIL_E_SVCUNSUPPORTED,
  RIL_E_UNKNOWNSUBSCRIBER,
  RIL_E_NETWKOUTOFORDER,
  RIL_E_NETWKTEMPFAILURE,
  RIL_E_CONGESTION,
  RIL_E_RESOURCESUNAVAILABLE,
  RIL_E_SVCNOTSUBSCRIBED,
  RIL_E_SVCNOTIMPLEMENTED,
  RIL_E_INVALIDMSGREFERENCE,
  RIL_E_INVALIDMSG,
  RIL_E_INVALIDMANDATORYINFO,
  RIL_E_MSGTYPEUNSUPPORTED,
  RIL_E_ICOMPATIBLEMSG,
  RIL_E_INFOELEMENTUNSUPPORTED,
  RIL_E_PROTOCOLERROR,
  RIL_E_NETWORKERROR,
  RIL_E_MESSAGINGERROR,
  RIL_E_NOTREADY,
  RIL_E_TIMEDOUT,
  RIL_E_CANCELLED,
  RIL_E_NONOTIFYCALLBACK,
  RIL_E_OPFMTUNAVAILABLE,
  RIL_E_NORESPONSETODIAL,
  RIL_E_SECURITYFAILURE,
  RIL_E_RADIOFAILEDINIT,
  RIL_E_DRIVERINITFAILED,
  RIL_E_RADIONOTPRESENT,
  RIL_E_RADIOOFF,
  RIL_E_ILLEGALMS,
  RIL_E_ILLEGALME,
  RIL_E_GPRSSERVICENOTALLOWED,
  RIL_E_PLMNNOTALLOWED,
  RIL_E_LOCATIONAREANOTALLOWED,
  RIL_E_ROAMINGNOTALLOWEDINTHISLOCATIONAREA,
  RIL_E_SERVICEOPTIONNOTSUPPORTED,
  RIL_E_REQUESTEDSERVICEOPTIONNOTSUBSCRIBED,
  RIL_E_SERVICEOPTIONTEMPORARILYOUTOFORDER,
  RIL_E_PDPAUTHENTICATIONFAILURE,
  RIL_E_INVALIDMOBILECLASS,
  RIL_E_UNSPECIFIEDGPRSERROR,
  RIL_E_RADIOREBOOTED,
  RIL_E_INVALIDCONTEXTSTATE,
  RIL_E_MAXCONTEXTS,
  RIL_E_SYNCHRONOUS_DATA_UNAVAILABLE,
  RIL_E_FDNRESTRICT,
  RIL_E_INVALIDASYNCCOMMANDRESPONSE,
  RIL_E_INCOMPATIBLEPROXYDRIVER,
  RIL_E_INVALIDDRIVERVERSION,
  RIL_E_USIMCALLMODIFIED,
  RIL_E_PASSWORDMISMATCH,
  RIL_E_INVALIDCONTEXTACTIVATIONSTRING,
  RIL_E_UICCAPPINACCESSIBLE,
  RIL_E_UICCPINREQUIRED,
  RIL_E_UICCPUKREQUIRED,
  RIL_E_UICCPUKBLOCKED,
  RIL_E_EXECUTORNOTREADY,
  RIL_E_INVALIDUICCKEYREF,
  RIL_E_UICCINACTIVE,
  RIL_E_PERSOPUKREQUIRED,
  RIL_E_PERSOPUKBLOCKED,
  RIL_E_PERSOCHECKFAILED,
  RIL_E_INVALIDUICCPATH,
  RIL_E_IMSTEMPFAILURE,
  RIL_E_UICCNOTREADY,
  RIL_E_UICCPOWEROFF,
  RIL_E_CALLISACTIVE,
  RIL_E_USIMCALLBLOCKED,
  RIL_E_UICCADMRESTRICTED,
  RIL_E_DMSERVICENOTREADY,
  RIL_E_DMGETCONFIGFAILED,
  RIL_E_DMCOMMITFAILED,
  RIL_E_OTHEREXECUTORBUSY,
  RIL_E_IMSNOHANDOVERTARGETFOUND,
  RIL_E_VCCHANDOVERINPROGRESS,
  RIL_E_INVALIDREMOTEURI,
  RIL_E_ECTNOTALLOWED,
  RIL_E_ECTCALLINCONF,
  RIL_E_ECTCALLNOTONHOLD,
  RIL_E_ECTNOTSUBSCRIBED,
  RIL_E_ECTUNAVAILABLE,
  RIL_E_ECTINCOMPATIBLE,
  RIL_E_ECTNOTSUPPORTED,
  RIL_E_ECTSYSTEMERROR,
  RIL_E_ECTNORESOURCE,
  RIL_E_ECTCALLBARRED,
  RIL_E_ECTUNKNOWN,
  RIL_E_IMSCALLISACTIVE
} RILERRORCODES;
````


## -enum-fields
<dl>

### -field <a id="RIL_E_NOCONNECTION"></a><a id="ril_e_noconnection"></a><b>RIL_E_NOCONNECTION</b>

<dd></dd>

### -field <a id="RIL_E_LINKRESERVED"></a><a id="ril_e_linkreserved"></a><b>RIL_E_LINKRESERVED</b>

<dd></dd>

### -field <a id="RIL_E_OPNOTALLOWED"></a><a id="ril_e_opnotallowed"></a><b>RIL_E_OPNOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_E_OPNOTSUPPORTED"></a><a id="ril_e_opnotsupported"></a><b>RIL_E_OPNOTSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_UICCNOTINSERTED"></a><a id="ril_e_uiccnotinserted"></a><b>RIL_E_UICCNOTINSERTED</b>

<dd></dd>

### -field <a id="RIL_E_UICCFAILURE"></a><a id="ril_e_uiccfailure"></a><b>RIL_E_UICCFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_UICCBUSY"></a><a id="ril_e_uiccbusy"></a><b>RIL_E_UICCBUSY</b>

<dd></dd>

### -field <a id="RIL_E_UICCWRONG"></a><a id="ril_e_uiccwrong"></a><b>RIL_E_UICCWRONG</b>

<dd></dd>

### -field <a id="RIL_E_INCORRECTPASSWORD"></a><a id="ril_e_incorrectpassword"></a><b>RIL_E_INCORRECTPASSWORD</b>

<dd></dd>

### -field <a id="RIL_E_MEMORYFULL"></a><a id="ril_e_memoryfull"></a><b>RIL_E_MEMORYFULL</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDINDEX"></a><a id="ril_e_invalidindex"></a><b>RIL_E_INVALIDINDEX</b>

<dd></dd>

### -field <a id="RIL_E_NOTFOUND"></a><a id="ril_e_notfound"></a><b>RIL_E_NOTFOUND</b>

<dd></dd>

### -field <a id="RIL_E_MEMORYFAILURE"></a><a id="ril_e_memoryfailure"></a><b>RIL_E_MEMORYFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_TEXTSTRINGTOOLONG"></a><a id="ril_e_textstringtoolong"></a><b>RIL_E_TEXTSTRINGTOOLONG</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDTEXTSTRING"></a><a id="ril_e_invalidtextstring"></a><b>RIL_E_INVALIDTEXTSTRING</b>

<dd></dd>

### -field <a id="RIL_E_DIALSTRINGTOOLONG"></a><a id="ril_e_dialstringtoolong"></a><b>RIL_E_DIALSTRINGTOOLONG</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDDIALSTRING"></a><a id="ril_e_invaliddialstring"></a><b>RIL_E_INVALIDDIALSTRING</b>

<dd></dd>

### -field <a id="RIL_E_NONETWORKSVC"></a><a id="ril_e_nonetworksvc"></a><b>RIL_E_NONETWORKSVC</b>

<dd></dd>

### -field <a id="RIL_E_NETWORKTIMEOUT"></a><a id="ril_e_networktimeout"></a><b>RIL_E_NETWORKTIMEOUT</b>

<dd></dd>

### -field <a id="RIL_E_EMERGENCYONLY"></a><a id="ril_e_emergencyonly"></a><b>RIL_E_EMERGENCYONLY</b>

<dd></dd>

### -field <a id="RIL_E_TELEMATICIWUNSUPPORTED"></a><a id="ril_e_telematiciwunsupported"></a><b>RIL_E_TELEMATICIWUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_SMTYPE0UNSUPPORTED"></a><a id="ril_e_smtype0unsupported"></a><b>RIL_E_SMTYPE0UNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_CANTREPLACEMSG"></a><a id="ril_e_cantreplacemsg"></a><b>RIL_E_CANTREPLACEMSG</b>

<dd></dd>

### -field <a id="RIL_E_PROTOCOLIDERROR"></a><a id="ril_e_protocoliderror"></a><b>RIL_E_PROTOCOLIDERROR</b>

<dd></dd>

### -field <a id="RIL_E_DCSUNSUPPORTED"></a><a id="ril_e_dcsunsupported"></a><b>RIL_E_DCSUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_MSGCLASSUNSUPPORTED"></a><a id="ril_e_msgclassunsupported"></a><b>RIL_E_MSGCLASSUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_DCSERROR"></a><a id="ril_e_dcserror"></a><b>RIL_E_DCSERROR</b>

<dd></dd>

### -field <a id="RIL_E_CMDCANTBEACTIONED"></a><a id="ril_e_cmdcantbeactioned"></a><b>RIL_E_CMDCANTBEACTIONED</b>

<dd></dd>

### -field <a id="RIL_E_CMDUNSUPPORTED"></a><a id="ril_e_cmdunsupported"></a><b>RIL_E_CMDUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_CMDERROR"></a><a id="ril_e_cmderror"></a><b>RIL_E_CMDERROR</b>

<dd></dd>

### -field <a id="RIL_E_MSGBODYHEADERERROR"></a><a id="ril_e_msgbodyheadererror"></a><b>RIL_E_MSGBODYHEADERERROR</b>

<dd></dd>

### -field <a id="RIL_E_SCBUSY"></a><a id="ril_e_scbusy"></a><b>RIL_E_SCBUSY</b>

<dd></dd>

### -field <a id="RIL_E_NOSCSUBSCRIPTION"></a><a id="ril_e_noscsubscription"></a><b>RIL_E_NOSCSUBSCRIPTION</b>

<dd></dd>

### -field <a id="RIL_E_SCSYSTEMFAILURE"></a><a id="ril_e_scsystemfailure"></a><b>RIL_E_SCSYSTEMFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDADDRESS"></a><a id="ril_e_invalidaddress"></a><b>RIL_E_INVALIDADDRESS</b>

<dd></dd>

### -field <a id="RIL_E_DESTINATIONBARRED"></a><a id="ril_e_destinationbarred"></a><b>RIL_E_DESTINATIONBARRED</b>

<dd></dd>

### -field <a id="RIL_E_REJECTEDDUPLICATE"></a><a id="ril_e_rejectedduplicate"></a><b>RIL_E_REJECTEDDUPLICATE</b>

<dd></dd>

### -field <a id="RIL_E_VPFUNSUPPORTED"></a><a id="ril_e_vpfunsupported"></a><b>RIL_E_VPFUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_VPUNSUPPORTED"></a><a id="ril_e_vpunsupported"></a><b>RIL_E_VPUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_UICCMSGSTORAGEFULL"></a><a id="ril_e_uiccmsgstoragefull"></a><b>RIL_E_UICCMSGSTORAGEFULL</b>

<dd></dd>

### -field <a id="RIL_E_NOUICCMSGSTORAGE"></a><a id="ril_e_nouiccmsgstorage"></a><b>RIL_E_NOUICCMSGSTORAGE</b>

<dd></dd>

### -field <a id="RIL_E_UICCTOOLKITBUSY"></a><a id="ril_e_uicctoolkitbusy"></a><b>RIL_E_UICCTOOLKITBUSY</b>

<dd></dd>

### -field <a id="RIL_E_UICCDOWNLOADERROR"></a><a id="ril_e_uiccdownloaderror"></a><b>RIL_E_UICCDOWNLOADERROR</b>

<dd></dd>

### -field <a id="RIL_E_MSGSVCRESERVED"></a><a id="ril_e_msgsvcreserved"></a><b>RIL_E_MSGSVCRESERVED</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDMSGPARAM"></a><a id="ril_e_invalidmsgparam"></a><b>RIL_E_INVALIDMSGPARAM</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDSCADDRESS"></a><a id="ril_e_invalidscaddress"></a><b>RIL_E_INVALIDSCADDRESS</b>

<dd></dd>

### -field <a id="RIL_E_UNASSIGNEDNUMBER"></a><a id="ril_e_unassignednumber"></a><b>RIL_E_UNASSIGNEDNUMBER</b>

<dd></dd>

### -field <a id="RIL_E_MSGBARREDBYOPERATOR"></a><a id="ril_e_msgbarredbyoperator"></a><b>RIL_E_MSGBARREDBYOPERATOR</b>

<dd></dd>

### -field <a id="RIL_E_MSGCALLBARRED"></a><a id="ril_e_msgcallbarred"></a><b>RIL_E_MSGCALLBARRED</b>

<dd></dd>

### -field <a id="RIL_E_MSGXFERREJECTED"></a><a id="ril_e_msgxferrejected"></a><b>RIL_E_MSGXFERREJECTED</b>

<dd></dd>

### -field <a id="RIL_E_DESTINATIONOUTOFSVC"></a><a id="ril_e_destinationoutofsvc"></a><b>RIL_E_DESTINATIONOUTOFSVC</b>

<dd></dd>

### -field <a id="RIL_E_UNIDENTIFIEDSUBCRIBER"></a><a id="ril_e_unidentifiedsubcriber"></a><b>RIL_E_UNIDENTIFIEDSUBCRIBER</b>

<dd></dd>

### -field <a id="RIL_E_SVCUNSUPPORTED"></a><a id="ril_e_svcunsupported"></a><b>RIL_E_SVCUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_UNKNOWNSUBSCRIBER"></a><a id="ril_e_unknownsubscriber"></a><b>RIL_E_UNKNOWNSUBSCRIBER</b>

<dd></dd>

### -field <a id="RIL_E_NETWKOUTOFORDER"></a><a id="ril_e_netwkoutoforder"></a><b>RIL_E_NETWKOUTOFORDER</b>

<dd></dd>

### -field <a id="RIL_E_NETWKTEMPFAILURE"></a><a id="ril_e_netwktempfailure"></a><b>RIL_E_NETWKTEMPFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_CONGESTION"></a><a id="ril_e_congestion"></a><b>RIL_E_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_E_RESOURCESUNAVAILABLE"></a><a id="ril_e_resourcesunavailable"></a><b>RIL_E_RESOURCESUNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_E_SVCNOTSUBSCRIBED"></a><a id="ril_e_svcnotsubscribed"></a><b>RIL_E_SVCNOTSUBSCRIBED</b>

<dd></dd>

### -field <a id="RIL_E_SVCNOTIMPLEMENTED"></a><a id="ril_e_svcnotimplemented"></a><b>RIL_E_SVCNOTIMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDMSGREFERENCE"></a><a id="ril_e_invalidmsgreference"></a><b>RIL_E_INVALIDMSGREFERENCE</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDMSG"></a><a id="ril_e_invalidmsg"></a><b>RIL_E_INVALIDMSG</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDMANDATORYINFO"></a><a id="ril_e_invalidmandatoryinfo"></a><b>RIL_E_INVALIDMANDATORYINFO</b>

<dd></dd>

### -field <a id="RIL_E_MSGTYPEUNSUPPORTED"></a><a id="ril_e_msgtypeunsupported"></a><b>RIL_E_MSGTYPEUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_ICOMPATIBLEMSG"></a><a id="ril_e_icompatiblemsg"></a><b>RIL_E_ICOMPATIBLEMSG</b>

<dd></dd>

### -field <a id="RIL_E_INFOELEMENTUNSUPPORTED"></a><a id="ril_e_infoelementunsupported"></a><b>RIL_E_INFOELEMENTUNSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_PROTOCOLERROR"></a><a id="ril_e_protocolerror"></a><b>RIL_E_PROTOCOLERROR</b>

<dd></dd>

### -field <a id="RIL_E_NETWORKERROR"></a><a id="ril_e_networkerror"></a><b>RIL_E_NETWORKERROR</b>

<dd></dd>

### -field <a id="RIL_E_MESSAGINGERROR"></a><a id="ril_e_messagingerror"></a><b>RIL_E_MESSAGINGERROR</b>

<dd></dd>

### -field <a id="RIL_E_NOTREADY"></a><a id="ril_e_notready"></a><b>RIL_E_NOTREADY</b>

<dd></dd>

### -field <a id="RIL_E_TIMEDOUT"></a><a id="ril_e_timedout"></a><b>RIL_E_TIMEDOUT</b>

<dd></dd>

### -field <a id="RIL_E_CANCELLED"></a><a id="ril_e_cancelled"></a><b>RIL_E_CANCELLED</b>

<dd></dd>

### -field <a id="RIL_E_NONOTIFYCALLBACK"></a><a id="ril_e_nonotifycallback"></a><b>RIL_E_NONOTIFYCALLBACK</b>

<dd></dd>

### -field <a id="RIL_E_OPFMTUNAVAILABLE"></a><a id="ril_e_opfmtunavailable"></a><b>RIL_E_OPFMTUNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_E_NORESPONSETODIAL"></a><a id="ril_e_noresponsetodial"></a><b>RIL_E_NORESPONSETODIAL</b>

<dd></dd>

### -field <a id="RIL_E_SECURITYFAILURE"></a><a id="ril_e_securityfailure"></a><b>RIL_E_SECURITYFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_RADIOFAILEDINIT"></a><a id="ril_e_radiofailedinit"></a><b>RIL_E_RADIOFAILEDINIT</b>

<dd></dd>

### -field <a id="RIL_E_DRIVERINITFAILED"></a><a id="ril_e_driverinitfailed"></a><b>RIL_E_DRIVERINITFAILED</b>

<dd></dd>

### -field <a id="RIL_E_RADIONOTPRESENT"></a><a id="ril_e_radionotpresent"></a><b>RIL_E_RADIONOTPRESENT</b>

<dd></dd>

### -field <a id="RIL_E_RADIOOFF"></a><a id="ril_e_radiooff"></a><b>RIL_E_RADIOOFF</b>

<dd></dd>

### -field <a id="RIL_E_ILLEGALMS"></a><a id="ril_e_illegalms"></a><b>RIL_E_ILLEGALMS</b>

<dd></dd>

### -field <a id="RIL_E_ILLEGALME"></a><a id="ril_e_illegalme"></a><b>RIL_E_ILLEGALME</b>

<dd></dd>

### -field <a id="RIL_E_GPRSSERVICENOTALLOWED"></a><a id="ril_e_gprsservicenotallowed"></a><b>RIL_E_GPRSSERVICENOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_E_PLMNNOTALLOWED"></a><a id="ril_e_plmnnotallowed"></a><b>RIL_E_PLMNNOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_E_LOCATIONAREANOTALLOWED"></a><a id="ril_e_locationareanotallowed"></a><b>RIL_E_LOCATIONAREANOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_E_ROAMINGNOTALLOWEDINTHISLOCATIONAREA"></a><a id="ril_e_roamingnotallowedinthislocationarea"></a><b>RIL_E_ROAMINGNOTALLOWEDINTHISLOCATIONAREA</b>

<dd></dd>

### -field <a id="RIL_E_SERVICEOPTIONNOTSUPPORTED"></a><a id="ril_e_serviceoptionnotsupported"></a><b>RIL_E_SERVICEOPTIONNOTSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_REQUESTEDSERVICEOPTIONNOTSUBSCRIBED"></a><a id="ril_e_requestedserviceoptionnotsubscribed"></a><b>RIL_E_REQUESTEDSERVICEOPTIONNOTSUBSCRIBED</b>

<dd></dd>

### -field <a id="RIL_E_SERVICEOPTIONTEMPORARILYOUTOFORDER"></a><a id="ril_e_serviceoptiontemporarilyoutoforder"></a><b>RIL_E_SERVICEOPTIONTEMPORARILYOUTOFORDER</b>

<dd></dd>

### -field <a id="RIL_E_PDPAUTHENTICATIONFAILURE"></a><a id="ril_e_pdpauthenticationfailure"></a><b>RIL_E_PDPAUTHENTICATIONFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDMOBILECLASS"></a><a id="ril_e_invalidmobileclass"></a><b>RIL_E_INVALIDMOBILECLASS</b>

<dd></dd>

### -field <a id="RIL_E_UNSPECIFIEDGPRSERROR"></a><a id="ril_e_unspecifiedgprserror"></a><b>RIL_E_UNSPECIFIEDGPRSERROR</b>

<dd></dd>

### -field <a id="RIL_E_RADIOREBOOTED"></a><a id="ril_e_radiorebooted"></a><b>RIL_E_RADIOREBOOTED</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDCONTEXTSTATE"></a><a id="ril_e_invalidcontextstate"></a><b>RIL_E_INVALIDCONTEXTSTATE</b>

<dd></dd>

### -field <a id="RIL_E_MAXCONTEXTS"></a><a id="ril_e_maxcontexts"></a><b>RIL_E_MAXCONTEXTS</b>

<dd></dd>

### -field <a id="RIL_E_SYNCHRONOUS_DATA_UNAVAILABLE"></a><a id="ril_e_synchronous_data_unavailable"></a><b>RIL_E_SYNCHRONOUS_DATA_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_E_FDNRESTRICT"></a><a id="ril_e_fdnrestrict"></a><b>RIL_E_FDNRESTRICT</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDASYNCCOMMANDRESPONSE"></a><a id="ril_e_invalidasynccommandresponse"></a><b>RIL_E_INVALIDASYNCCOMMANDRESPONSE</b>

<dd></dd>

### -field <a id="RIL_E_INCOMPATIBLEPROXYDRIVER"></a><a id="ril_e_incompatibleproxydriver"></a><b>RIL_E_INCOMPATIBLEPROXYDRIVER</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDDRIVERVERSION"></a><a id="ril_e_invaliddriverversion"></a><b>RIL_E_INVALIDDRIVERVERSION</b>

<dd></dd>

### -field <a id="RIL_E_USIMCALLMODIFIED"></a><a id="ril_e_usimcallmodified"></a><b>RIL_E_USIMCALLMODIFIED</b>

<dd></dd>

### -field <a id="RIL_E_PASSWORDMISMATCH"></a><a id="ril_e_passwordmismatch"></a><b>RIL_E_PASSWORDMISMATCH</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDCONTEXTACTIVATIONSTRING"></a><a id="ril_e_invalidcontextactivationstring"></a><b>RIL_E_INVALIDCONTEXTACTIVATIONSTRING</b>

<dd></dd>

### -field <a id="RIL_E_UICCAPPINACCESSIBLE"></a><a id="ril_e_uiccappinaccessible"></a><b>RIL_E_UICCAPPINACCESSIBLE</b>

<dd></dd>

### -field <a id="RIL_E_UICCPINREQUIRED"></a><a id="ril_e_uiccpinrequired"></a><b>RIL_E_UICCPINREQUIRED</b>

<dd></dd>

### -field <a id="RIL_E_UICCPUKREQUIRED"></a><a id="ril_e_uiccpukrequired"></a><b>RIL_E_UICCPUKREQUIRED</b>

<dd></dd>

### -field <a id="RIL_E_UICCPUKBLOCKED"></a><a id="ril_e_uiccpukblocked"></a><b>RIL_E_UICCPUKBLOCKED</b>

<dd></dd>

### -field <a id="RIL_E_EXECUTORNOTREADY"></a><a id="ril_e_executornotready"></a><b>RIL_E_EXECUTORNOTREADY</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDUICCKEYREF"></a><a id="ril_e_invaliduicckeyref"></a><b>RIL_E_INVALIDUICCKEYREF</b>

<dd></dd>

### -field <a id="RIL_E_UICCINACTIVE"></a><a id="ril_e_uiccinactive"></a><b>RIL_E_UICCINACTIVE</b>

<dd></dd>

### -field <a id="RIL_E_PERSOPUKREQUIRED"></a><a id="ril_e_persopukrequired"></a><b>RIL_E_PERSOPUKREQUIRED</b>

<dd></dd>

### -field <a id="RIL_E_PERSOPUKBLOCKED"></a><a id="ril_e_persopukblocked"></a><b>RIL_E_PERSOPUKBLOCKED</b>

<dd></dd>

### -field <a id="RIL_E_PERSOCHECKFAILED"></a><a id="ril_e_persocheckfailed"></a><b>RIL_E_PERSOCHECKFAILED</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDUICCPATH"></a><a id="ril_e_invaliduiccpath"></a><b>RIL_E_INVALIDUICCPATH</b>

<dd></dd>

### -field <a id="RIL_E_IMSTEMPFAILURE"></a><a id="ril_e_imstempfailure"></a><b>RIL_E_IMSTEMPFAILURE</b>

<dd></dd>

### -field <a id="RIL_E_UICCNOTREADY"></a><a id="ril_e_uiccnotready"></a><b>RIL_E_UICCNOTREADY</b>

<dd></dd>

### -field <a id="RIL_E_UICCPOWEROFF"></a><a id="ril_e_uiccpoweroff"></a><b>RIL_E_UICCPOWEROFF</b>

<dd></dd>

### -field <a id="RIL_E_CALLISACTIVE"></a><a id="ril_e_callisactive"></a><b>RIL_E_CALLISACTIVE</b>

<dd></dd>

### -field <a id="RIL_E_USIMCALLBLOCKED"></a><a id="ril_e_usimcallblocked"></a><b>RIL_E_USIMCALLBLOCKED</b>

<dd></dd>

### -field <a id="RIL_E_UICCADMRESTRICTED"></a><a id="ril_e_uiccadmrestricted"></a><b>RIL_E_UICCADMRESTRICTED</b>

<dd></dd>

### -field <a id="RIL_E_DMSERVICENOTREADY"></a><a id="ril_e_dmservicenotready"></a><b>RIL_E_DMSERVICENOTREADY</b>

<dd></dd>

### -field <a id="RIL_E_DMGETCONFIGFAILED"></a><a id="ril_e_dmgetconfigfailed"></a><b>RIL_E_DMGETCONFIGFAILED</b>

<dd></dd>

### -field <a id="RIL_E_DMCOMMITFAILED"></a><a id="ril_e_dmcommitfailed"></a><b>RIL_E_DMCOMMITFAILED</b>

<dd></dd>

### -field <a id="RIL_E_OTHEREXECUTORBUSY"></a><a id="ril_e_otherexecutorbusy"></a><b>RIL_E_OTHEREXECUTORBUSY</b>

<dd></dd>

### -field <a id="RIL_E_IMSNOHANDOVERTARGETFOUND"></a><a id="ril_e_imsnohandovertargetfound"></a><b>RIL_E_IMSNOHANDOVERTARGETFOUND</b>

<dd></dd>

### -field <a id="RIL_E_VCCHANDOVERINPROGRESS"></a><a id="ril_e_vcchandoverinprogress"></a><b>RIL_E_VCCHANDOVERINPROGRESS</b>

<dd></dd>

### -field <a id="RIL_E_INVALIDREMOTEURI"></a><a id="ril_e_invalidremoteuri"></a><b>RIL_E_INVALIDREMOTEURI</b>

<dd></dd>

### -field <a id="RIL_E_ECTNOTALLOWED"></a><a id="ril_e_ectnotallowed"></a><b>RIL_E_ECTNOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_E_ECTCALLINCONF"></a><a id="ril_e_ectcallinconf"></a><b>RIL_E_ECTCALLINCONF</b>

<dd></dd>

### -field <a id="RIL_E_ECTCALLNOTONHOLD"></a><a id="ril_e_ectcallnotonhold"></a><b>RIL_E_ECTCALLNOTONHOLD</b>

<dd></dd>

### -field <a id="RIL_E_ECTNOTSUBSCRIBED"></a><a id="ril_e_ectnotsubscribed"></a><b>RIL_E_ECTNOTSUBSCRIBED</b>

<dd></dd>

### -field <a id="RIL_E_ECTUNAVAILABLE"></a><a id="ril_e_ectunavailable"></a><b>RIL_E_ECTUNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_E_ECTINCOMPATIBLE"></a><a id="ril_e_ectincompatible"></a><b>RIL_E_ECTINCOMPATIBLE</b>

<dd></dd>

### -field <a id="RIL_E_ECTNOTSUPPORTED"></a><a id="ril_e_ectnotsupported"></a><b>RIL_E_ECTNOTSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_E_ECTSYSTEMERROR"></a><a id="ril_e_ectsystemerror"></a><b>RIL_E_ECTSYSTEMERROR</b>

<dd></dd>

### -field <a id="RIL_E_ECTNORESOURCE"></a><a id="ril_e_ectnoresource"></a><b>RIL_E_ECTNORESOURCE</b>

<dd></dd>

### -field <a id="RIL_E_ECTCALLBARRED"></a><a id="ril_e_ectcallbarred"></a><b>RIL_E_ECTCALLBARRED</b>

<dd></dd>

### -field <a id="RIL_E_ECTUNKNOWN"></a><a id="ril_e_ectunknown"></a><b>RIL_E_ECTUNKNOWN</b>

<dd></dd>

### -field <a id="RIL_E_IMSCALLISACTIVE"></a><a id="ril_e_imscallisactive"></a><b>RIL_E_IMSCALLISACTIVE</b>

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