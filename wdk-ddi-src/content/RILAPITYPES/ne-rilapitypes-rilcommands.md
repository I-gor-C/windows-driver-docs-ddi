---
UID: NE.rilapitypes.RILCOMMANDS
title: RILCOMMANDS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcommands_2.htm
ms.assetid: 16fe6a2d-c0bd-49ab-9f23-20664cfb3f6f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCOMMANDS
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILCOMMANDS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCOMMANDS { 
  RIL_COMMAND_GETNEXTNOTIFICATION,
  RIL_COMMAND_ENABLENOTIFICATIONS,
  RIL_COMMAND_DISABLENOTIFICATIONS,
  RIL_COMMAND_GETDRIVERVERSION,
  RIL_COMMAND_GETDEVCAPS,
  RIL_COMMAND_GETDEVICEINFO,
  RIL_COMMAND_GETEQUIPMENTSTATE,
  RIL_COMMAND_SETEQUIPMENTSTATE,
  RIL_COMMAND_SETNOTIFICATIONFILTERSTATE,
  RIL_COMMAND_GETNOTIFICATIONFILTERSTATE,
  RIL_COMMAND_ENUMERATESLOTS,
  RIL_COMMAND_GETCARDINFO,
  RIL_COMMAND_SETSLOTPOWER,
  RIL_COMMAND_GETUICCRECORDSTATUS,
  RIL_COMMAND_SENDRESTRICTEDUICCCMD,
  RIL_COMMAND_WATCHUICCFILECHANGE,
  RIL_COMMAND_GETUICCPRLID,
  RIL_COMMAND_GETIMSI,
  RIL_COMMAND_GETSUBSCRIBERNUMBERS,
  RIL_COMMAND_GETUICCLOCKSTATE,
  RIL_COMMAND_GETUICCSERVICELOCK,
  RIL_COMMAND_VERIFYUICCLOCK,
  RIL_COMMAND_SETUICCLOCKENABLED,
  RIL_COMMAND_UNBLOCKUICCLOCK,
  RIL_COMMAND_CHANGEUICCLOCKPASSWORD,
  RIL_COMMAND_GETUICCAPPPERSOCHECKSTATE,
  RIL_COMMAND_GETPERSODEACTIVATIONSTATE,
  RIL_COMMAND_DEACTIVATEPERSO,
  RIL_COMMAND_READPHONEBOOKENTRIES,
  RIL_COMMAND_WRITEPHONEBOOKENTRY,
  RIL_COMMAND_DELETEPHONEBOOKENTRY,
  RIL_COMMAND_GETPHONEBOOKOPTIONS,
  RIL_COMMAND_GETALLADDITIONALNUMBERSTRINGS,
  RIL_COMMAND_GETALLEMERGENCYNUMBERS,
  RIL_COMMAND_SETRADIOCONFIGURATION,
  RIL_COMMAND_GETRADIOCONFIGURATION,
  RIL_COMMAND_SETEXECUTORCONFIG,
  RIL_COMMAND_GETEXECUTORCONFIG,
  RIL_COMMAND_SETSYSTEMSELECTIONPREFS,
  RIL_COMMAND_GETSYSTEMSELECTIONPREFS,
  RIL_COMMAND_GETOPERATORLIST,
  RIL_COMMAND_GETPREFERREDOPERATORLIST,
  RIL_COMMAND_GETCURRENTREGSTATUS,
  RIL_COMMAND_GETSIGNALQUALITY,
  RIL_COMMAND_SENDUICCTOOLKITCMDRESPONSE,
  RIL_COMMAND_SENDUICCTOOLKITENVELOPE,
  RIL_COMMAND_DIAL,
  RIL_COMMAND_MANAGECALLS,
  RIL_COMMAND_EMERGENCYMODECONTROL,
  RIL_COMMAND_GETCALLFORWARDINGSETTINGS,
  RIL_COMMAND_SETCALLFORWARDINGSTATUS,
  RIL_COMMAND_ADDCALLFORWARDING,
  RIL_COMMAND_REMOVECALLFORWARDING,
  RIL_COMMAND_GETCALLBARRINGSTATUS,
  RIL_COMMAND_SETCALLBARRINGSTATUS,
  RIL_COMMAND_CHANGECALLBARRINGPASSWORD,
  RIL_COMMAND_GETCALLWAITINGSETTINGS,
  RIL_COMMAND_SETCALLWAITINGSTATUS,
  RIL_COMMAND_GETCALLERIDSETTINGS,
  RIL_COMMAND_GETDIALEDIDSETTINGS,
  RIL_COMMAND_GETHIDECONNECTEDIDSETTINGS,
  RIL_COMMAND_GETHIDEIDSETTINGS,
  RIL_COMMAND_SENDFLASH,
  RIL_COMMAND_SENDSUPSERVICEDATA,
  RIL_COMMAND_SENDDTMF,
  RIL_COMMAND_STARTDTMF,
  RIL_COMMAND_STOPDTMF,
  RIL_COMMAND_GETMSGSERVICEOPTIONS,
  RIL_COMMAND_READMSG,
  RIL_COMMAND_WRITEMSG,
  RIL_COMMAND_DELETEMSG,
  RIL_COMMAND_GETCELLBROADCASTMSGCONFIG,
  RIL_COMMAND_SETCELLBROADCASTMSGCONFIG,
  RIL_COMMAND_GETMSGINUICCSTATUS,
  RIL_COMMAND_SETMSGINUICCSTATUS,
  RIL_COMMAND_SETMSGMEMORYSTATUS,
  RIL_COMMAND_SENDMSG,
  RIL_COMMAND_GETSMSC,
  RIL_COMMAND_SETSMSC,
  RIL_COMMAND_GETIMSSTATUS,
  RIL_COMMAND_GETPOSITIONINFO,
  RIL_COMMAND_GETRADIOSTATEGROUPS,
  RIL_COMMAND_GETRADIOSTATEDETAILS,
  RIL_COMMAND_SETRADIOSTATEDETAILS,
  RIL_COMMAND_RADIOSTATEPASSWORDCOMPARE,
  RIL_COMMAND_RADIOSTATEGETPASSWORDRETRYCOUNT,
  RIL_COMMAND_DEVSPECIFIC,
  RIL_COMMAND_SETRFSTATE,
  RIL_COMMAND_GETRFSTATE,
  RIL_COMMAND_GETDMPROFILECONFIGINFO,
  RIL_COMMAND_SETDMPROFILECONFIGINFO,
  RIL_COMMAND_WRITEADDITIONALNUMBERSTRING,
  RIL_COMMAND_DELETEADDITIONALNUMBERSTRING,
  RIL_COMMAND_GETUICCATR,
  RIL_COMMAND_OPENUICCLOGICALCHANNEL,
  RIL_COMMAND_CLOSEUICCLOGICALCHANNEL,
  RIL_COMMAND_EXCHANGEUICCAPDU,
  RIL_COMMAND_SENDSUPSERVICEDATARESPONSE,
  RIL_COMMAND_CANCELSUPSERVICEDATASESSION,
  RIL_COMMAND_SETUICCTOOLKITPROFILE,
  RIL_COMMAND_GETUICCTOOLKITPROFILE,
  RIL_COMMAND_REGISTERUICCTOOLKITSERVICE,
  RIL_COMMAND_SENDMSGACK,
  RIL_COMMAND_CLOSEUICCLOGICALCHANNELGROUP,
  RIL_COMMAND_SETPREFERREDOPERATORLIST,
  RIL_COMMAND_GETUICCSERVICESTATE,
  RIL_COMMAND_SETUICCSERVICESTATE,
  RIL_COMMAND_GETCALLLIST,
  RIL_COMMAND_GETEXECUTORFOCUS,
  RIL_COMMAND_SETEXECUTORFOCUS,
  RIL_COMMAND_GETEMERGENCYMODE,
  RIL_COMMAND_GETEXECUTORRFSTATE,
  RIL_COMMAND_SETEXECUTORRFSTATE,
  RIL_COMMAND_RESETMODEM,
  RIL_COMMAND_CANCELGETOPERATORLIST,
  RIL_COMMAND_AVOIDCDMASYSTEM,
  RIL_COMMAND_SETPSMEDIACONFIGURATION,
  RIL_COMMAND_GETPSMEDIACONFIGURATION,
  RIL_COMMAND_SETGEOLOCATIONDATA,
  RIL_COMMAND_SETTERMINALCAPABILITY,
  RIL_COMMAND_GETTERMINALCAPABILITY,
  RIL_COMMAND_SENDRTT,
  RIL_COMMAND_ENABLEMODEMFILTERS,
  RIL_COMMAND_DISABLEMODEMFILTERS,
  RIL_COMMAND_STARTMODEMLOGS,
  RIL_COMMAND_STOPMODEMLOGS,
  RIL_COMMAND_DRAINMODEMLOGS,
  RIL_COMMAND_COUNT
} RILCOMMANDS;
````


## -enum-fields
<dl>

### -field <a id="RIL_COMMAND_GETNEXTNOTIFICATION"></a><a id="ril_command_getnextnotification"></a><b>RIL_COMMAND_GETNEXTNOTIFICATION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_ENABLENOTIFICATIONS"></a><a id="ril_command_enablenotifications"></a><b>RIL_COMMAND_ENABLENOTIFICATIONS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DISABLENOTIFICATIONS"></a><a id="ril_command_disablenotifications"></a><b>RIL_COMMAND_DISABLENOTIFICATIONS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETDRIVERVERSION"></a><a id="ril_command_getdriverversion"></a><b>RIL_COMMAND_GETDRIVERVERSION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETDEVCAPS"></a><a id="ril_command_getdevcaps"></a><b>RIL_COMMAND_GETDEVCAPS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETDEVICEINFO"></a><a id="ril_command_getdeviceinfo"></a><b>RIL_COMMAND_GETDEVICEINFO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETEQUIPMENTSTATE"></a><a id="ril_command_getequipmentstate"></a><b>RIL_COMMAND_GETEQUIPMENTSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETEQUIPMENTSTATE"></a><a id="ril_command_setequipmentstate"></a><b>RIL_COMMAND_SETEQUIPMENTSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETNOTIFICATIONFILTERSTATE"></a><a id="ril_command_setnotificationfilterstate"></a><b>RIL_COMMAND_SETNOTIFICATIONFILTERSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETNOTIFICATIONFILTERSTATE"></a><a id="ril_command_getnotificationfilterstate"></a><b>RIL_COMMAND_GETNOTIFICATIONFILTERSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_ENUMERATESLOTS"></a><a id="ril_command_enumerateslots"></a><b>RIL_COMMAND_ENUMERATESLOTS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCARDINFO"></a><a id="ril_command_getcardinfo"></a><b>RIL_COMMAND_GETCARDINFO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETSLOTPOWER"></a><a id="ril_command_setslotpower"></a><b>RIL_COMMAND_SETSLOTPOWER</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCRECORDSTATUS"></a><a id="ril_command_getuiccrecordstatus"></a><b>RIL_COMMAND_GETUICCRECORDSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDRESTRICTEDUICCCMD"></a><a id="ril_command_sendrestricteduicccmd"></a><b>RIL_COMMAND_SENDRESTRICTEDUICCCMD</b>

<dd></dd>

### -field <a id="RIL_COMMAND_WATCHUICCFILECHANGE"></a><a id="ril_command_watchuiccfilechange"></a><b>RIL_COMMAND_WATCHUICCFILECHANGE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCPRLID"></a><a id="ril_command_getuiccprlid"></a><b>RIL_COMMAND_GETUICCPRLID</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETIMSI"></a><a id="ril_command_getimsi"></a><b>RIL_COMMAND_GETIMSI</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETSUBSCRIBERNUMBERS"></a><a id="ril_command_getsubscribernumbers"></a><b>RIL_COMMAND_GETSUBSCRIBERNUMBERS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCLOCKSTATE"></a><a id="ril_command_getuicclockstate"></a><b>RIL_COMMAND_GETUICCLOCKSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCSERVICELOCK"></a><a id="ril_command_getuiccservicelock"></a><b>RIL_COMMAND_GETUICCSERVICELOCK</b>

<dd></dd>

### -field <a id="RIL_COMMAND_VERIFYUICCLOCK"></a><a id="ril_command_verifyuicclock"></a><b>RIL_COMMAND_VERIFYUICCLOCK</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETUICCLOCKENABLED"></a><a id="ril_command_setuicclockenabled"></a><b>RIL_COMMAND_SETUICCLOCKENABLED</b>

<dd></dd>

### -field <a id="RIL_COMMAND_UNBLOCKUICCLOCK"></a><a id="ril_command_unblockuicclock"></a><b>RIL_COMMAND_UNBLOCKUICCLOCK</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CHANGEUICCLOCKPASSWORD"></a><a id="ril_command_changeuicclockpassword"></a><b>RIL_COMMAND_CHANGEUICCLOCKPASSWORD</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCAPPPERSOCHECKSTATE"></a><a id="ril_command_getuiccapppersocheckstate"></a><b>RIL_COMMAND_GETUICCAPPPERSOCHECKSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETPERSODEACTIVATIONSTATE"></a><a id="ril_command_getpersodeactivationstate"></a><b>RIL_COMMAND_GETPERSODEACTIVATIONSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DEACTIVATEPERSO"></a><a id="ril_command_deactivateperso"></a><b>RIL_COMMAND_DEACTIVATEPERSO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_READPHONEBOOKENTRIES"></a><a id="ril_command_readphonebookentries"></a><b>RIL_COMMAND_READPHONEBOOKENTRIES</b>

<dd></dd>

### -field <a id="RIL_COMMAND_WRITEPHONEBOOKENTRY"></a><a id="ril_command_writephonebookentry"></a><b>RIL_COMMAND_WRITEPHONEBOOKENTRY</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DELETEPHONEBOOKENTRY"></a><a id="ril_command_deletephonebookentry"></a><b>RIL_COMMAND_DELETEPHONEBOOKENTRY</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETPHONEBOOKOPTIONS"></a><a id="ril_command_getphonebookoptions"></a><b>RIL_COMMAND_GETPHONEBOOKOPTIONS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETALLADDITIONALNUMBERSTRINGS"></a><a id="ril_command_getalladditionalnumberstrings"></a><b>RIL_COMMAND_GETALLADDITIONALNUMBERSTRINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETALLEMERGENCYNUMBERS"></a><a id="ril_command_getallemergencynumbers"></a><b>RIL_COMMAND_GETALLEMERGENCYNUMBERS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETRADIOCONFIGURATION"></a><a id="ril_command_setradioconfiguration"></a><b>RIL_COMMAND_SETRADIOCONFIGURATION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETRADIOCONFIGURATION"></a><a id="ril_command_getradioconfiguration"></a><b>RIL_COMMAND_GETRADIOCONFIGURATION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETEXECUTORCONFIG"></a><a id="ril_command_setexecutorconfig"></a><b>RIL_COMMAND_SETEXECUTORCONFIG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETEXECUTORCONFIG"></a><a id="ril_command_getexecutorconfig"></a><b>RIL_COMMAND_GETEXECUTORCONFIG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETSYSTEMSELECTIONPREFS"></a><a id="ril_command_setsystemselectionprefs"></a><b>RIL_COMMAND_SETSYSTEMSELECTIONPREFS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETSYSTEMSELECTIONPREFS"></a><a id="ril_command_getsystemselectionprefs"></a><b>RIL_COMMAND_GETSYSTEMSELECTIONPREFS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETOPERATORLIST"></a><a id="ril_command_getoperatorlist"></a><b>RIL_COMMAND_GETOPERATORLIST</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETPREFERREDOPERATORLIST"></a><a id="ril_command_getpreferredoperatorlist"></a><b>RIL_COMMAND_GETPREFERREDOPERATORLIST</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCURRENTREGSTATUS"></a><a id="ril_command_getcurrentregstatus"></a><b>RIL_COMMAND_GETCURRENTREGSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETSIGNALQUALITY"></a><a id="ril_command_getsignalquality"></a><b>RIL_COMMAND_GETSIGNALQUALITY</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDUICCTOOLKITCMDRESPONSE"></a><a id="ril_command_senduicctoolkitcmdresponse"></a><b>RIL_COMMAND_SENDUICCTOOLKITCMDRESPONSE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDUICCTOOLKITENVELOPE"></a><a id="ril_command_senduicctoolkitenvelope"></a><b>RIL_COMMAND_SENDUICCTOOLKITENVELOPE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DIAL"></a><a id="ril_command_dial"></a><b>RIL_COMMAND_DIAL</b>

<dd></dd>

### -field <a id="RIL_COMMAND_MANAGECALLS"></a><a id="ril_command_managecalls"></a><b>RIL_COMMAND_MANAGECALLS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_EMERGENCYMODECONTROL"></a><a id="ril_command_emergencymodecontrol"></a><b>RIL_COMMAND_EMERGENCYMODECONTROL</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCALLFORWARDINGSETTINGS"></a><a id="ril_command_getcallforwardingsettings"></a><b>RIL_COMMAND_GETCALLFORWARDINGSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETCALLFORWARDINGSTATUS"></a><a id="ril_command_setcallforwardingstatus"></a><b>RIL_COMMAND_SETCALLFORWARDINGSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_ADDCALLFORWARDING"></a><a id="ril_command_addcallforwarding"></a><b>RIL_COMMAND_ADDCALLFORWARDING</b>

<dd></dd>

### -field <a id="RIL_COMMAND_REMOVECALLFORWARDING"></a><a id="ril_command_removecallforwarding"></a><b>RIL_COMMAND_REMOVECALLFORWARDING</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCALLBARRINGSTATUS"></a><a id="ril_command_getcallbarringstatus"></a><b>RIL_COMMAND_GETCALLBARRINGSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETCALLBARRINGSTATUS"></a><a id="ril_command_setcallbarringstatus"></a><b>RIL_COMMAND_SETCALLBARRINGSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CHANGECALLBARRINGPASSWORD"></a><a id="ril_command_changecallbarringpassword"></a><b>RIL_COMMAND_CHANGECALLBARRINGPASSWORD</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCALLWAITINGSETTINGS"></a><a id="ril_command_getcallwaitingsettings"></a><b>RIL_COMMAND_GETCALLWAITINGSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETCALLWAITINGSTATUS"></a><a id="ril_command_setcallwaitingstatus"></a><b>RIL_COMMAND_SETCALLWAITINGSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCALLERIDSETTINGS"></a><a id="ril_command_getcalleridsettings"></a><b>RIL_COMMAND_GETCALLERIDSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETDIALEDIDSETTINGS"></a><a id="ril_command_getdialedidsettings"></a><b>RIL_COMMAND_GETDIALEDIDSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETHIDECONNECTEDIDSETTINGS"></a><a id="ril_command_gethideconnectedidsettings"></a><b>RIL_COMMAND_GETHIDECONNECTEDIDSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETHIDEIDSETTINGS"></a><a id="ril_command_gethideidsettings"></a><b>RIL_COMMAND_GETHIDEIDSETTINGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDFLASH"></a><a id="ril_command_sendflash"></a><b>RIL_COMMAND_SENDFLASH</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDSUPSERVICEDATA"></a><a id="ril_command_sendsupservicedata"></a><b>RIL_COMMAND_SENDSUPSERVICEDATA</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDDTMF"></a><a id="ril_command_senddtmf"></a><b>RIL_COMMAND_SENDDTMF</b>

<dd></dd>

### -field <a id="RIL_COMMAND_STARTDTMF"></a><a id="ril_command_startdtmf"></a><b>RIL_COMMAND_STARTDTMF</b>

<dd></dd>

### -field <a id="RIL_COMMAND_STOPDTMF"></a><a id="ril_command_stopdtmf"></a><b>RIL_COMMAND_STOPDTMF</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETMSGSERVICEOPTIONS"></a><a id="ril_command_getmsgserviceoptions"></a><b>RIL_COMMAND_GETMSGSERVICEOPTIONS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_READMSG"></a><a id="ril_command_readmsg"></a><b>RIL_COMMAND_READMSG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_WRITEMSG"></a><a id="ril_command_writemsg"></a><b>RIL_COMMAND_WRITEMSG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DELETEMSG"></a><a id="ril_command_deletemsg"></a><b>RIL_COMMAND_DELETEMSG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCELLBROADCASTMSGCONFIG"></a><a id="ril_command_getcellbroadcastmsgconfig"></a><b>RIL_COMMAND_GETCELLBROADCASTMSGCONFIG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETCELLBROADCASTMSGCONFIG"></a><a id="ril_command_setcellbroadcastmsgconfig"></a><b>RIL_COMMAND_SETCELLBROADCASTMSGCONFIG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETMSGINUICCSTATUS"></a><a id="ril_command_getmsginuiccstatus"></a><b>RIL_COMMAND_GETMSGINUICCSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETMSGINUICCSTATUS"></a><a id="ril_command_setmsginuiccstatus"></a><b>RIL_COMMAND_SETMSGINUICCSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETMSGMEMORYSTATUS"></a><a id="ril_command_setmsgmemorystatus"></a><b>RIL_COMMAND_SETMSGMEMORYSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDMSG"></a><a id="ril_command_sendmsg"></a><b>RIL_COMMAND_SENDMSG</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETSMSC"></a><a id="ril_command_getsmsc"></a><b>RIL_COMMAND_GETSMSC</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETSMSC"></a><a id="ril_command_setsmsc"></a><b>RIL_COMMAND_SETSMSC</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETIMSSTATUS"></a><a id="ril_command_getimsstatus"></a><b>RIL_COMMAND_GETIMSSTATUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETPOSITIONINFO"></a><a id="ril_command_getpositioninfo"></a><b>RIL_COMMAND_GETPOSITIONINFO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETRADIOSTATEGROUPS"></a><a id="ril_command_getradiostategroups"></a><b>RIL_COMMAND_GETRADIOSTATEGROUPS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETRADIOSTATEDETAILS"></a><a id="ril_command_getradiostatedetails"></a><b>RIL_COMMAND_GETRADIOSTATEDETAILS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETRADIOSTATEDETAILS"></a><a id="ril_command_setradiostatedetails"></a><b>RIL_COMMAND_SETRADIOSTATEDETAILS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_RADIOSTATEPASSWORDCOMPARE"></a><a id="ril_command_radiostatepasswordcompare"></a><b>RIL_COMMAND_RADIOSTATEPASSWORDCOMPARE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_RADIOSTATEGETPASSWORDRETRYCOUNT"></a><a id="ril_command_radiostategetpasswordretrycount"></a><b>RIL_COMMAND_RADIOSTATEGETPASSWORDRETRYCOUNT</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DEVSPECIFIC"></a><a id="ril_command_devspecific"></a><b>RIL_COMMAND_DEVSPECIFIC</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETRFSTATE"></a><a id="ril_command_setrfstate"></a><b>RIL_COMMAND_SETRFSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETRFSTATE"></a><a id="ril_command_getrfstate"></a><b>RIL_COMMAND_GETRFSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETDMPROFILECONFIGINFO"></a><a id="ril_command_getdmprofileconfiginfo"></a><b>RIL_COMMAND_GETDMPROFILECONFIGINFO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETDMPROFILECONFIGINFO"></a><a id="ril_command_setdmprofileconfiginfo"></a><b>RIL_COMMAND_SETDMPROFILECONFIGINFO</b>

<dd></dd>

### -field <a id="RIL_COMMAND_WRITEADDITIONALNUMBERSTRING"></a><a id="ril_command_writeadditionalnumberstring"></a><b>RIL_COMMAND_WRITEADDITIONALNUMBERSTRING</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DELETEADDITIONALNUMBERSTRING"></a><a id="ril_command_deleteadditionalnumberstring"></a><b>RIL_COMMAND_DELETEADDITIONALNUMBERSTRING</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCATR"></a><a id="ril_command_getuiccatr"></a><b>RIL_COMMAND_GETUICCATR</b>

<dd></dd>

### -field <a id="RIL_COMMAND_OPENUICCLOGICALCHANNEL"></a><a id="ril_command_openuicclogicalchannel"></a><b>RIL_COMMAND_OPENUICCLOGICALCHANNEL</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CLOSEUICCLOGICALCHANNEL"></a><a id="ril_command_closeuicclogicalchannel"></a><b>RIL_COMMAND_CLOSEUICCLOGICALCHANNEL</b>

<dd></dd>

### -field <a id="RIL_COMMAND_EXCHANGEUICCAPDU"></a><a id="ril_command_exchangeuiccapdu"></a><b>RIL_COMMAND_EXCHANGEUICCAPDU</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDSUPSERVICEDATARESPONSE"></a><a id="ril_command_sendsupservicedataresponse"></a><b>RIL_COMMAND_SENDSUPSERVICEDATARESPONSE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CANCELSUPSERVICEDATASESSION"></a><a id="ril_command_cancelsupservicedatasession"></a><b>RIL_COMMAND_CANCELSUPSERVICEDATASESSION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETUICCTOOLKITPROFILE"></a><a id="ril_command_setuicctoolkitprofile"></a><b>RIL_COMMAND_SETUICCTOOLKITPROFILE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCTOOLKITPROFILE"></a><a id="ril_command_getuicctoolkitprofile"></a><b>RIL_COMMAND_GETUICCTOOLKITPROFILE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_REGISTERUICCTOOLKITSERVICE"></a><a id="ril_command_registeruicctoolkitservice"></a><b>RIL_COMMAND_REGISTERUICCTOOLKITSERVICE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDMSGACK"></a><a id="ril_command_sendmsgack"></a><b>RIL_COMMAND_SENDMSGACK</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CLOSEUICCLOGICALCHANNELGROUP"></a><a id="ril_command_closeuicclogicalchannelgroup"></a><b>RIL_COMMAND_CLOSEUICCLOGICALCHANNELGROUP</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETPREFERREDOPERATORLIST"></a><a id="ril_command_setpreferredoperatorlist"></a><b>RIL_COMMAND_SETPREFERREDOPERATORLIST</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETUICCSERVICESTATE"></a><a id="ril_command_getuiccservicestate"></a><b>RIL_COMMAND_GETUICCSERVICESTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETUICCSERVICESTATE"></a><a id="ril_command_setuiccservicestate"></a><b>RIL_COMMAND_SETUICCSERVICESTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETCALLLIST"></a><a id="ril_command_getcalllist"></a><b>RIL_COMMAND_GETCALLLIST</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETEXECUTORFOCUS"></a><a id="ril_command_getexecutorfocus"></a><b>RIL_COMMAND_GETEXECUTORFOCUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETEXECUTORFOCUS"></a><a id="ril_command_setexecutorfocus"></a><b>RIL_COMMAND_SETEXECUTORFOCUS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETEMERGENCYMODE"></a><a id="ril_command_getemergencymode"></a><b>RIL_COMMAND_GETEMERGENCYMODE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETEXECUTORRFSTATE"></a><a id="ril_command_getexecutorrfstate"></a><b>RIL_COMMAND_GETEXECUTORRFSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETEXECUTORRFSTATE"></a><a id="ril_command_setexecutorrfstate"></a><b>RIL_COMMAND_SETEXECUTORRFSTATE</b>

<dd></dd>

### -field <a id="RIL_COMMAND_RESETMODEM"></a><a id="ril_command_resetmodem"></a><b>RIL_COMMAND_RESETMODEM</b>

<dd></dd>

### -field <a id="RIL_COMMAND_CANCELGETOPERATORLIST"></a><a id="ril_command_cancelgetoperatorlist"></a><b>RIL_COMMAND_CANCELGETOPERATORLIST</b>

<dd></dd>

### -field <a id="RIL_COMMAND_AVOIDCDMASYSTEM"></a><a id="ril_command_avoidcdmasystem"></a><b>RIL_COMMAND_AVOIDCDMASYSTEM</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETPSMEDIACONFIGURATION"></a><a id="ril_command_setpsmediaconfiguration"></a><b>RIL_COMMAND_SETPSMEDIACONFIGURATION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETPSMEDIACONFIGURATION"></a><a id="ril_command_getpsmediaconfiguration"></a><b>RIL_COMMAND_GETPSMEDIACONFIGURATION</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETGEOLOCATIONDATA"></a><a id="ril_command_setgeolocationdata"></a><b>RIL_COMMAND_SETGEOLOCATIONDATA</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SETTERMINALCAPABILITY"></a><a id="ril_command_setterminalcapability"></a><b>RIL_COMMAND_SETTERMINALCAPABILITY</b>

<dd></dd>

### -field <a id="RIL_COMMAND_GETTERMINALCAPABILITY"></a><a id="ril_command_getterminalcapability"></a><b>RIL_COMMAND_GETTERMINALCAPABILITY</b>

<dd></dd>

### -field <a id="RIL_COMMAND_SENDRTT"></a><a id="ril_command_sendrtt"></a><b>RIL_COMMAND_SENDRTT</b>

<dd></dd>

### -field <a id="RIL_COMMAND_ENABLEMODEMFILTERS"></a><a id="ril_command_enablemodemfilters"></a><b>RIL_COMMAND_ENABLEMODEMFILTERS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DISABLEMODEMFILTERS"></a><a id="ril_command_disablemodemfilters"></a><b>RIL_COMMAND_DISABLEMODEMFILTERS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_STARTMODEMLOGS"></a><a id="ril_command_startmodemlogs"></a><b>RIL_COMMAND_STARTMODEMLOGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_STOPMODEMLOGS"></a><a id="ril_command_stopmodemlogs"></a><b>RIL_COMMAND_STOPMODEMLOGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_DRAINMODEMLOGS"></a><a id="ril_command_drainmodemlogs"></a><b>RIL_COMMAND_DRAINMODEMLOGS</b>

<dd></dd>

### -field <a id="RIL_COMMAND_COUNT"></a><a id="ril_command_count"></a><b>RIL_COMMAND_COUNT</b>

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