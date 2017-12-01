---
UID: NE.wdm.POWER_INFORMATION_LEVEL
title: POWER_INFORMATION_LEVEL
author: windows-driver-content
description: Indicates power level information.
old-location: kernel\power_information_level.htm
old-project: kernel
ms.assetid: DCAB0482-C0E3-4F75-B5A7-FB8DFFA89D6F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POWER_INFORMATION_LEVEL
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# POWER_INFORMATION_LEVEL enumeration



## -description
<p>Indicates power level information.</p>


## -syntax

````
typedef enum _POWER_INFORMATION_LEVEL { 
  SystemPowerPolicyAc,
  SystemPowerPolicyDc,
  VerifySystemPolicyAc,
  VerifySystemPolicyDc,
  SystemPowerCapabilities,
  SystemBatteryState,
  SystemPowerStateHandler,
  ProcessorStateHandler,
  SystemPowerPolicyCurrent,
  AdministratorPowerPolicy,
  SystemReserveHiberFile,
  ProcessorInformation,
  SystemPowerInformation,
  ProcessorStateHandler2,
  LastWakeTime,
  LastSleepTime,
  SystemExecutionState,
  SystemPowerStateNotifyHandler,
  ProcessorPowerPolicyAc,
  ProcessorPowerPolicyDc,
  VerifyProcessorPowerPolicyAc,
  VerifyProcessorPowerPolicyDc,
  ProcessorPowerPolicyCurrent,
  SystemPowerStateLogging,
  SystemPowerLoggingEntry,
  SetPowerSettingValue,
  NotifyUserPowerSetting,
  PowerInformationLevelUnused0,
  SystemMonitorHiberBootPowerOff,
  SystemVideoState,
  TraceApplicationPowerMessage,
  TraceApplicationPowerMessageEnd,
  ProcessorPerfStates,
  ProcessorIdleStates,
  ProcessorCap,
  SystemWakeSource,
  SystemHiberFileInformation,
  TraceServicePowerMessage,
  ProcessorLoad,
  PowerShutdownNotification,
  MonitorCapabilities,
  SessionPowerInit,
  SessionDisplayState,
  PowerRequestCreate,
  PowerRequestAction,
  GetPowerRequestList,
  ProcessorInformationEx,
  NotifyUserModeLegacyPowerEvent,
  GroupPark,
  ProcessorIdleDomains,
  WakeTimerList,
  SystemHiberFileSize,
  ProcessorIdleStatesHv,
  ProcessorPerfStatesHv,
  ProcessorPerfCapHv,
  ProcessorSetIdle,
  LogicalProcessorIdling,
  UserPresence,
  PowerSettingNotificationName,
  GetPowerSettingValue,
  IdleResiliency,
  SessionRITState,
  SessionConnectNotification,
  SessionPowerCleanup,
  SessionLockState,
  SystemHiberbootState,
  PlatformInformation,
  PdcInvocation,
  MonitorInvocation,
  FirmwareTableInformationRegistered,
  SetShutdownSelectedTime,
  SuspendResumeInvocation,
  PlmPowerRequestCreate,
  ScreenOff,
  CsDeviceNotification,
  PlatformRole,
  LastResumePerformance,
  DisplayBurst,
  ExitLatencySamplingPercentage,
  RegisterSpmPowerSettings,
  PlatformIdleStates,
  ProcessorIdleVeto,
  PlatformIdleVeto,
  SystemBatteryStatePrecise,
  ThermalEvent,
  PowerRequestActionInternal,
  BatteryDeviceState,
  PowerInformationInternal,
  ThermalStandby,
  SystemHiberFileType,
  PhysicalPowerButtonPress,
  QueryPotentialDripsConstraint,
  EnergyTrackerCreate,
  EnergyTrackerQuery,
  UpdateBlackBoxRecorder,
  PowerInformationLevelMaximum
} POWER_INFORMATION_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="SystemPowerPolicyAc"></a><a id="systempowerpolicyac"></a><a id="SYSTEMPOWERPOLICYAC"></a><b>SystemPowerPolicyAc</b>

<dd>
<p>Indicates SystemPowerPolicyAc.</p>
</dd>

### -field <a id="SystemPowerPolicyDc"></a><a id="systempowerpolicydc"></a><a id="SYSTEMPOWERPOLICYDC"></a><b>SystemPowerPolicyDc</b>

<dd>
<p>Indicates SystemPowerPolicyDc.</p>
</dd>

### -field <a id="VerifySystemPolicyAc"></a><a id="verifysystempolicyac"></a><a id="VERIFYSYSTEMPOLICYAC"></a><b>VerifySystemPolicyAc</b>

<dd>
<p>Indicates VerifySystemPolicyAc.</p>
</dd>

### -field <a id="VerifySystemPolicyDc"></a><a id="verifysystempolicydc"></a><a id="VERIFYSYSTEMPOLICYDC"></a><b>VerifySystemPolicyDc</b>

<dd>
<p>Indicates VerifySystemPolicyDc.</p>
</dd>

### -field <a id="SystemPowerCapabilities"></a><a id="systempowercapabilities"></a><a id="SYSTEMPOWERCAPABILITIES"></a><b>SystemPowerCapabilities</b>

<dd>
<p>Indicates the power capabilities of the system.</p>
</dd>

### -field <a id="SystemBatteryState"></a><a id="systembatterystate"></a><a id="SYSTEMBATTERYSTATE"></a><b>SystemBatteryState</b>

<dd>
<p>Indicates the system's battery state.</p>
</dd>

### -field <a id="SystemPowerStateHandler"></a><a id="systempowerstatehandler"></a><a id="SYSTEMPOWERSTATEHANDLER"></a><b>SystemPowerStateHandler</b>

<dd>
<p>Indicates the system's power state handler.</p>
</dd>

### -field <a id="ProcessorStateHandler"></a><a id="processorstatehandler"></a><a id="PROCESSORSTATEHANDLER"></a><b>ProcessorStateHandler</b>

<dd>
<p>Indicates the processor state handler.</p>
</dd>

### -field <a id="SystemPowerPolicyCurrent"></a><a id="systempowerpolicycurrent"></a><a id="SYSTEMPOWERPOLICYCURRENT"></a><b>SystemPowerPolicyCurrent</b>

<dd>
<p>Indicates the system's current power policy.</p>
</dd>

### -field <a id="AdministratorPowerPolicy"></a><a id="administratorpowerpolicy"></a><a id="ADMINISTRATORPOWERPOLICY"></a><b>AdministratorPowerPolicy</b>

<dd>
<p>Indicates the administrator's power policy.</p>
</dd>

### -field <a id="SystemReserveHiberFile"></a><a id="systemreservehiberfile"></a><a id="SYSTEMRESERVEHIBERFILE"></a><b>SystemReserveHiberFile</b>

<dd>
<p>Indicates the SystemReserveHiberFile.</p>
</dd>

### -field <a id="ProcessorInformation"></a><a id="processorinformation"></a><a id="PROCESSORINFORMATION"></a><b>ProcessorInformation</b>

<dd>
<p>Indicates the processor information.</p>
</dd>

### -field <a id="SystemPowerInformation"></a><a id="systempowerinformation"></a><a id="SYSTEMPOWERINFORMATION"></a><b>SystemPowerInformation</b>

<dd>
<p>Indicates the system power information.</p>
</dd>

### -field <a id="ProcessorStateHandler2"></a><a id="processorstatehandler2"></a><a id="PROCESSORSTATEHANDLER2"></a><b>ProcessorStateHandler2</b>

<dd>
<p>Indicates the processor state handler.</p>
</dd>

### -field <a id="LastWakeTime"></a><a id="lastwaketime"></a><a id="LASTWAKETIME"></a><b>LastWakeTime</b>

<dd>
<p>Indicates the last wake time.</p>
</dd>

### -field <a id="LastSleepTime"></a><a id="lastsleeptime"></a><a id="LASTSLEEPTIME"></a><b>LastSleepTime</b>

<dd>
<p>Indicates the last sleep time.</p>
</dd>

### -field <a id="SystemExecutionState"></a><a id="systemexecutionstate"></a><a id="SYSTEMEXECUTIONSTATE"></a><b>SystemExecutionState</b>

<dd>
<p>Indicates the system execution state.</p>
</dd>

### -field <a id="SystemPowerStateNotifyHandler"></a><a id="systempowerstatenotifyhandler"></a><a id="SYSTEMPOWERSTATENOTIFYHANDLER"></a><b>SystemPowerStateNotifyHandler</b>

<dd>
<p>Indicates the system power state notify handler.</p>
</dd>

### -field <a id="ProcessorPowerPolicyAc"></a><a id="processorpowerpolicyac"></a><a id="PROCESSORPOWERPOLICYAC"></a><b>ProcessorPowerPolicyAc</b>

<dd>
<p>Indicates ProcessorPowerPolicyAc.</p>
</dd>

### -field <a id="ProcessorPowerPolicyDc"></a><a id="processorpowerpolicydc"></a><a id="PROCESSORPOWERPOLICYDC"></a><b>ProcessorPowerPolicyDc</b>

<dd>
<p>Indicates ProcessorPowerPolicyDc.</p>
</dd>

### -field <a id="VerifyProcessorPowerPolicyAc"></a><a id="verifyprocessorpowerpolicyac"></a><a id="VERIFYPROCESSORPOWERPOLICYAC"></a><b>VerifyProcessorPowerPolicyAc</b>

<dd>
<p>Indicates VerifyProcessorPowerPolicyAc.</p>
</dd>

### -field <a id="VerifyProcessorPowerPolicyDc"></a><a id="verifyprocessorpowerpolicydc"></a><a id="VERIFYPROCESSORPOWERPOLICYDC"></a><b>VerifyProcessorPowerPolicyDc</b>

<dd>
<p>Indicates VerifyProcessorPowerPolicyDc.</p>
</dd>

### -field <a id="ProcessorPowerPolicyCurrent"></a><a id="processorpowerpolicycurrent"></a><a id="PROCESSORPOWERPOLICYCURRENT"></a><b>ProcessorPowerPolicyCurrent</b>

<dd>
<p>Indicates the current processor power policy.</p>
</dd>

### -field <a id="SystemPowerStateLogging"></a><a id="systempowerstatelogging"></a><a id="SYSTEMPOWERSTATELOGGING"></a><b>SystemPowerStateLogging</b>

<dd>
<p>Indicates SystemPowerStateLogging.</p>
</dd>

### -field <a id="SystemPowerLoggingEntry"></a><a id="systempowerloggingentry"></a><a id="SYSTEMPOWERLOGGINGENTRY"></a><b>SystemPowerLoggingEntry</b>

<dd>
<p>Indicates SystemPowerLoggingEntry.</p>
</dd>

### -field <a id="SetPowerSettingValue"></a><a id="setpowersettingvalue"></a><a id="SETPOWERSETTINGVALUE"></a><b>SetPowerSettingValue</b>

<dd>
<p>Indicates that the power setting value is set.</p>
</dd>

### -field <a id="NotifyUserPowerSetting"></a><a id="notifyuserpowersetting"></a><a id="NOTIFYUSERPOWERSETTING"></a><b>NotifyUserPowerSetting</b>

<dd>
<p>Indicates that the user should be notified of the power setting.</p>
</dd>

### -field <a id="PowerInformationLevelUnused0"></a><a id="powerinformationlevelunused0"></a><a id="POWERINFORMATIONLEVELUNUSED0"></a><b>PowerInformationLevelUnused0</b>

<dd>
<p>Indicates that the power information level is unused.</p>
</dd>

### -field <a id="SystemMonitorHiberBootPowerOff"></a><a id="systemmonitorhiberbootpoweroff"></a><a id="SYSTEMMONITORHIBERBOOTPOWEROFF"></a><b>SystemMonitorHiberBootPowerOff</b>

<dd>
<p>Indicates that the system monitor boot power is off.</p>
</dd>

### -field <a id="SystemVideoState"></a><a id="systemvideostate"></a><a id="SYSTEMVIDEOSTATE"></a><b>SystemVideoState</b>

<dd>
<p>Indicates the system video state.</p>
</dd>

### -field <a id="TraceApplicationPowerMessage"></a><a id="traceapplicationpowermessage"></a><a id="TRACEAPPLICATIONPOWERMESSAGE"></a><b>TraceApplicationPowerMessage</b>

<dd>
<p>Indicates the trace application power message.</p>
</dd>

### -field <a id="TraceApplicationPowerMessageEnd"></a><a id="traceapplicationpowermessageend"></a><a id="TRACEAPPLICATIONPOWERMESSAGEEND"></a><b>TraceApplicationPowerMessageEnd</b>

<dd>
<p>Indicates the end of the trace application power message.</p>
</dd>

### -field <a id="ProcessorPerfStates"></a><a id="processorperfstates"></a><a id="PROCESSORPERFSTATES"></a><b>ProcessorPerfStates</b>

<dd>
<p>Indicates the processor performance states.</p>
</dd>

### -field <a id="ProcessorIdleStates"></a><a id="processoridlestates"></a><a id="PROCESSORIDLESTATES"></a><b>ProcessorIdleStates</b>

<dd>
<p>Indicates the processor idle states.</p>
</dd>

### -field <a id="ProcessorCap"></a><a id="processorcap"></a><a id="PROCESSORCAP"></a><b>ProcessorCap</b>

<dd>
<p>Indicates the processor cap.</p>
</dd>

### -field <a id="SystemWakeSource"></a><a id="systemwakesource"></a><a id="SYSTEMWAKESOURCE"></a><b>SystemWakeSource</b>

<dd>
<p>Indicates the system wake source.</p>
</dd>

### -field <a id="SystemHiberFileInformation"></a><a id="systemhiberfileinformation"></a><a id="SYSTEMHIBERFILEINFORMATION"></a><b>SystemHiberFileInformation</b>

<dd>
<p>Indicates the system's hibernation file information.</p>
</dd>

### -field <a id="TraceServicePowerMessage"></a><a id="traceservicepowermessage"></a><a id="TRACESERVICEPOWERMESSAGE"></a><b>TraceServicePowerMessage</b>

<dd>
<p>Indicates the trace service power message.</p>
</dd>

### -field <a id="ProcessorLoad"></a><a id="processorload"></a><a id="PROCESSORLOAD"></a><b>ProcessorLoad</b>

<dd>
<p>Indicates the processor load.</p>
</dd>

### -field <a id="PowerShutdownNotification"></a><a id="powershutdownnotification"></a><a id="POWERSHUTDOWNNOTIFICATION"></a><b>PowerShutdownNotification</b>

<dd>
<p>Indicates the power shutdown notification.</p>
</dd>

### -field <a id="MonitorCapabilities"></a><a id="monitorcapabilities"></a><a id="MONITORCAPABILITIES"></a><b>MonitorCapabilities</b>

<dd>
<p>Indicates the monitor's capabilities.</p>
</dd>

### -field <a id="SessionPowerInit"></a><a id="sessionpowerinit"></a><a id="SESSIONPOWERINIT"></a><b>SessionPowerInit</b>

<dd>
<p>Indicates the session power has been initialized.</p>
</dd>

### -field <a id="SessionDisplayState"></a><a id="sessiondisplaystate"></a><a id="SESSIONDISPLAYSTATE"></a><b>SessionDisplayState</b>

<dd>
<p>Indicates the session display state.</p>
</dd>

### -field <a id="PowerRequestCreate"></a><a id="powerrequestcreate"></a><a id="POWERREQUESTCREATE"></a><b>PowerRequestCreate</b>

<dd>
<p>Indicates that a power request has been created.</p>
</dd>

### -field <a id="PowerRequestAction"></a><a id="powerrequestaction"></a><a id="POWERREQUESTACTION"></a><b>PowerRequestAction</b>

<dd>
<p>Indicates the action of the power request.</p>
</dd>

### -field <a id="GetPowerRequestList"></a><a id="getpowerrequestlist"></a><a id="GETPOWERREQUESTLIST"></a><b>GetPowerRequestList</b>

<dd>
<p>Indicates that the power request list should be queued. </p>
</dd>

### -field <a id="ProcessorInformationEx"></a><a id="processorinformationex"></a><a id="PROCESSORINFORMATIONEX"></a><b>ProcessorInformationEx</b>

<dd>
<p>Indicates ProcessorInformationEx.</p>
</dd>

### -field <a id="NotifyUserModeLegacyPowerEvent"></a><a id="notifyusermodelegacypowerevent"></a><a id="NOTIFYUSERMODELEGACYPOWEREVENT"></a><b>NotifyUserModeLegacyPowerEvent</b>

<dd>
<p>Indicates that a notification should be created for the user mode legacy power event.</p>
</dd>

### -field <a id="GroupPark"></a><a id="grouppark"></a><a id="GROUPPARK"></a><b>GroupPark</b>

<dd>
<p>Indicates the group park.</p>
</dd>

### -field <a id="ProcessorIdleDomains"></a><a id="processoridledomains"></a><a id="PROCESSORIDLEDOMAINS"></a><b>ProcessorIdleDomains</b>

<dd>
<p>Indicates the processor's idle domains.</p>
</dd>

### -field <a id="WakeTimerList"></a><a id="waketimerlist"></a><a id="WAKETIMERLIST"></a><b>WakeTimerList</b>

<dd>
<p>Indicates the wake timer list.</p>
</dd>

### -field <a id="SystemHiberFileSize"></a><a id="systemhiberfilesize"></a><a id="SYSTEMHIBERFILESIZE"></a><b>SystemHiberFileSize</b>

<dd>
<p>Indicates the system's hibernation file size.</p>
</dd>

### -field <a id="ProcessorIdleStatesHv"></a><a id="processoridlestateshv"></a><a id="PROCESSORIDLESTATESHV"></a><b>ProcessorIdleStatesHv</b>

<dd>
<p>Indicates the processor's idle states.</p>
</dd>

### -field <a id="ProcessorPerfStatesHv"></a><a id="processorperfstateshv"></a><a id="PROCESSORPERFSTATESHV"></a><b>ProcessorPerfStatesHv</b>

<dd>
<p>Indicates the processor's performance states.</p>
</dd>

### -field <a id="ProcessorPerfCapHv"></a><a id="processorperfcaphv"></a><a id="PROCESSORPERFCAPHV"></a><b>ProcessorPerfCapHv</b>

<dd>
<p>Indicates the processor's performance capabilities.</p>
</dd>

### -field <a id="ProcessorSetIdle"></a><a id="processorsetidle"></a><a id="PROCESSORSETIDLE"></a><b>ProcessorSetIdle</b>

<dd>
<p>Indicates that the processor has been set to idle.</p>
</dd>

### -field <a id="LogicalProcessorIdling"></a><a id="logicalprocessoridling"></a><a id="LOGICALPROCESSORIDLING"></a><b>LogicalProcessorIdling</b>

<dd>
<p>Indicates that the processor is idling.</p>
</dd>

### -field <a id="UserPresence"></a><a id="userpresence"></a><a id="USERPRESENCE"></a><b>UserPresence</b>

<dd>
<p>Indicates the user presence.</p>
</dd>

### -field <a id="PowerSettingNotificationName"></a><a id="powersettingnotificationname"></a><a id="POWERSETTINGNOTIFICATIONNAME"></a><b>PowerSettingNotificationName</b>

<dd>
<p>Indicates the power setting notification name.</p>
</dd>

### -field <a id="GetPowerSettingValue"></a><a id="getpowersettingvalue"></a><a id="GETPOWERSETTINGVALUE"></a><b>GetPowerSettingValue</b>

<dd>
<p>Indicates that the power setting value should be queued.</p>
</dd>

### -field <a id="IdleResiliency"></a><a id="idleresiliency"></a><a id="IDLERESILIENCY"></a><b>IdleResiliency</b>

<dd>
<p>Indicates the idle resiliency.</p>
</dd>

### -field <a id="SessionRITState"></a><a id="sessionritstate"></a><a id="SESSIONRITSTATE"></a><b>SessionRITState</b>

<dd>
<p>Indicates the session's RIT state.</p>
</dd>

### -field <a id="SessionConnectNotification"></a><a id="sessionconnectnotification"></a><a id="SESSIONCONNECTNOTIFICATION"></a><b>SessionConnectNotification</b>

<dd>
<p>Indicates the session's connect notification.</p>
</dd>

### -field <a id="SessionPowerCleanup"></a><a id="sessionpowercleanup"></a><a id="SESSIONPOWERCLEANUP"></a><b>SessionPowerCleanup</b>

<dd>
<p>Indicates the session's power cleanup.</p>
</dd>

### -field <a id="SessionLockState"></a><a id="sessionlockstate"></a><a id="SESSIONLOCKSTATE"></a><b>SessionLockState</b>

<dd>
<p>Indicates the session's lock state.</p>
</dd>

### -field <a id="SystemHiberbootState"></a><a id="systemhiberbootstate"></a><a id="SYSTEMHIBERBOOTSTATE"></a><b>SystemHiberbootState</b>

<dd>
<p>Indicates the system's hibernation boot state.</p>
</dd>

### -field <a id="PlatformInformation"></a><a id="platforminformation"></a><a id="PLATFORMINFORMATION"></a><b>PlatformInformation</b>

<dd>
<p>Indicates the platform information.</p>
</dd>

### -field <a id="PdcInvocation"></a><a id="pdcinvocation"></a><a id="PDCINVOCATION"></a><b>PdcInvocation</b>

<dd>
<p>Indicates the pdc invocation.</p>
</dd>

### -field <a id="MonitorInvocation"></a><a id="monitorinvocation"></a><a id="MONITORINVOCATION"></a><b>MonitorInvocation</b>

<dd>
<p>Indicates the monitor invocation.</p>
</dd>

### -field <a id="FirmwareTableInformationRegistered"></a><a id="firmwaretableinformationregistered"></a><a id="FIRMWARETABLEINFORMATIONREGISTERED"></a><b>FirmwareTableInformationRegistered</b>

<dd>
<p>Indicates the registered firmware table information.</p>
</dd>

### -field <a id="SetShutdownSelectedTime"></a><a id="setshutdownselectedtime"></a><a id="SETSHUTDOWNSELECTEDTIME"></a><b>SetShutdownSelectedTime</b>

<dd>
<p>Indicates that the shutdown time should be set.</p>
</dd>

### -field <a id="SuspendResumeInvocation"></a><a id="suspendresumeinvocation"></a><a id="SUSPENDRESUMEINVOCATION"></a><b>SuspendResumeInvocation</b>

<dd>
<p>Indicates SuspendResumeInvocation.</p>
</dd>

### -field <a id="PlmPowerRequestCreate"></a><a id="plmpowerrequestcreate"></a><a id="PLMPOWERREQUESTCREATE"></a><b>PlmPowerRequestCreate</b>

<dd>
<p>Indicates that the power request has been created.</p>
</dd>

### -field <a id="ScreenOff"></a><a id="screenoff"></a><a id="SCREENOFF"></a><b>ScreenOff</b>

<dd>
<p>Indicates that the screen is off.</p>
</dd>

### -field <a id="CsDeviceNotification"></a><a id="csdevicenotification"></a><a id="CSDEVICENOTIFICATION"></a><b>CsDeviceNotification</b>

<dd>
<p>Indicates the device notification.</p>
</dd>

### -field <a id="PlatformRole"></a><a id="platformrole"></a><a id="PLATFORMROLE"></a><b>PlatformRole</b>

<dd>
<p>Indicates the platform role.</p>
</dd>

### -field <a id="LastResumePerformance"></a><a id="lastresumeperformance"></a><a id="LASTRESUMEPERFORMANCE"></a><b>LastResumePerformance</b>

<dd>
<p>Indicates the last time performance was resumed.</p>
</dd>

### -field <a id="DisplayBurst"></a><a id="displayburst"></a><a id="DISPLAYBURST"></a><b>DisplayBurst</b>

<dd>
<p>Indicates display burst.</p>
</dd>

### -field <a id="ExitLatencySamplingPercentage"></a><a id="exitlatencysamplingpercentage"></a><a id="EXITLATENCYSAMPLINGPERCENTAGE"></a><b>ExitLatencySamplingPercentage</b>

<dd>
<p>Indicates the latency sampling percentage.</p>
</dd>

### -field <a id="RegisterSpmPowerSettings"></a><a id="registerspmpowersettings"></a><a id="REGISTERSPMPOWERSETTINGS"></a><b>RegisterSpmPowerSettings</b>

<dd>
<p>Indicates that the power settings are registered.</p>
</dd>

### -field <a id="PlatformIdleStates"></a><a id="platformidlestates"></a><a id="PLATFORMIDLESTATES"></a><b>PlatformIdleStates</b>

<dd>
<p>Indicates the platform's idle states.</p>
</dd>

### -field <a id="ProcessorIdleVeto"></a><a id="processoridleveto"></a><a id="PROCESSORIDLEVETO"></a><b>ProcessorIdleVeto</b>

<dd>
<p>Indicates the processor's idle veto.</p>
</dd>

### -field <a id="PlatformIdleVeto"></a><a id="platformidleveto"></a><a id="PLATFORMIDLEVETO"></a><b>PlatformIdleVeto</b>

<dd>
<p>Indicates the platform's idle veto.</p>
</dd>

### -field <a id="SystemBatteryStatePrecise"></a><a id="systembatterystateprecise"></a><a id="SYSTEMBATTERYSTATEPRECISE"></a><b>SystemBatteryStatePrecise</b>

<dd>
<p>Indicates the system's battery state.</p>
</dd>

### -field <a id="ThermalEvent"></a><a id="thermalevent"></a><a id="THERMALEVENT"></a><b>ThermalEvent</b>

<dd>
<p>Indicates the thermal event.</p>
</dd>

### -field <a id="PowerRequestActionInternal"></a><a id="powerrequestactioninternal"></a><a id="POWERREQUESTACTIONINTERNAL"></a><b>PowerRequestActionInternal</b>

<dd>
<p>Indicates the internal power request action.</p>
</dd>

### -field <a id="BatteryDeviceState"></a><a id="batterydevicestate"></a><a id="BATTERYDEVICESTATE"></a><b>BatteryDeviceState</b>

<dd>
<p>Indicates the battery's device state.	</p>
</dd>

### -field <a id="PowerInformationInternal"></a><a id="powerinformationinternal"></a><a id="POWERINFORMATIONINTERNAL"></a><b>PowerInformationInternal</b>

<dd>
<p>Indicates the internal power information.</p>
</dd>

### -field <a id="ThermalStandby"></a><a id="thermalstandby"></a><a id="THERMALSTANDBY"></a><b>ThermalStandby</b>

<dd>
<p>Indicates thermal standby.</p>
</dd>

### -field <a id="SystemHiberFileType"></a><a id="systemhiberfiletype"></a><a id="SYSTEMHIBERFILETYPE"></a><b>SystemHiberFileType</b>

<dd>
<p>Indicates the system's hibernation file type.</p>
</dd>

### -field <a id="PhysicalPowerButtonPress"></a><a id="physicalpowerbuttonpress"></a><a id="PHYSICALPOWERBUTTONPRESS"></a><b>PhysicalPowerButtonPress</b>

<dd>
<p>Indicates a physical power button press.</p>
</dd>

### -field <a id="QueryPotentialDripsConstraint"></a><a id="querypotentialdripsconstraint"></a><a id="QUERYPOTENTIALDRIPSCONSTRAINT"></a><b>QueryPotentialDripsConstraint</b>

<dd>
<p>Indicates the potential drips constraint.</p>
</dd>

### -field <a id="EnergyTrackerCreate"></a><a id="energytrackercreate"></a><a id="ENERGYTRACKERCREATE"></a><b>EnergyTrackerCreate</b>

<dd>
<p>Indicates that the energy tracker is created.</p>
</dd>

### -field <a id="EnergyTrackerQuery"></a><a id="energytrackerquery"></a><a id="ENERGYTRACKERQUERY"></a><b>EnergyTrackerQuery</b>

<dd>
<p>Indicates that the energy tracker is queried.</p>
</dd>

### -field <a id="UpdateBlackBoxRecorder"></a><a id="updateblackboxrecorder"></a><a id="UPDATEBLACKBOXRECORDER"></a><b>UpdateBlackBoxRecorder</b>

<dd>
<p>Indicates that the black box recorder is updated.</p>
</dd>

### -field <a id="PowerInformationLevelMaximum"></a><a id="powerinformationlevelmaximum"></a><a id="POWERINFORMATIONLEVELMAXIMUM"></a><b>PowerInformationLevelMaximum</b>

<dd>
<p>Indicates the maximum power level.</p>
</dd>
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
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>