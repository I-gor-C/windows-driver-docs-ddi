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

### -field SystemPowerPolicyAc

<dd>
<p>Indicates SystemPowerPolicyAc.</p>
</dd>

### -field SystemPowerPolicyDc

<dd>
<p>Indicates SystemPowerPolicyDc.</p>
</dd>

### -field VerifySystemPolicyAc

<dd>
<p>Indicates VerifySystemPolicyAc.</p>
</dd>

### -field VerifySystemPolicyDc

<dd>
<p>Indicates VerifySystemPolicyDc.</p>
</dd>

### -field SystemPowerCapabilities

<dd>
<p>Indicates the power capabilities of the system.</p>
</dd>

### -field SystemBatteryState

<dd>
<p>Indicates the system's battery state.</p>
</dd>

### -field SystemPowerStateHandler

<dd>
<p>Indicates the system's power state handler.</p>
</dd>

### -field ProcessorStateHandler

<dd>
<p>Indicates the processor state handler.</p>
</dd>

### -field SystemPowerPolicyCurrent

<dd>
<p>Indicates the system's current power policy.</p>
</dd>

### -field AdministratorPowerPolicy

<dd>
<p>Indicates the administrator's power policy.</p>
</dd>

### -field SystemReserveHiberFile

<dd>
<p>Indicates the SystemReserveHiberFile.</p>
</dd>

### -field ProcessorInformation

<dd>
<p>Indicates the processor information.</p>
</dd>

### -field SystemPowerInformation

<dd>
<p>Indicates the system power information.</p>
</dd>

### -field ProcessorStateHandler2

<dd>
<p>Indicates the processor state handler.</p>
</dd>

### -field LastWakeTime

<dd>
<p>Indicates the last wake time.</p>
</dd>

### -field LastSleepTime

<dd>
<p>Indicates the last sleep time.</p>
</dd>

### -field SystemExecutionState

<dd>
<p>Indicates the system execution state.</p>
</dd>

### -field SystemPowerStateNotifyHandler

<dd>
<p>Indicates the system power state notify handler.</p>
</dd>

### -field ProcessorPowerPolicyAc

<dd>
<p>Indicates ProcessorPowerPolicyAc.</p>
</dd>

### -field ProcessorPowerPolicyDc

<dd>
<p>Indicates ProcessorPowerPolicyDc.</p>
</dd>

### -field VerifyProcessorPowerPolicyAc

<dd>
<p>Indicates VerifyProcessorPowerPolicyAc.</p>
</dd>

### -field VerifyProcessorPowerPolicyDc

<dd>
<p>Indicates VerifyProcessorPowerPolicyDc.</p>
</dd>

### -field ProcessorPowerPolicyCurrent

<dd>
<p>Indicates the current processor power policy.</p>
</dd>

### -field SystemPowerStateLogging

<dd>
<p>Indicates SystemPowerStateLogging.</p>
</dd>

### -field SystemPowerLoggingEntry

<dd>
<p>Indicates SystemPowerLoggingEntry.</p>
</dd>

### -field SetPowerSettingValue

<dd>
<p>Indicates that the power setting value is set.</p>
</dd>

### -field NotifyUserPowerSetting

<dd>
<p>Indicates that the user should be notified of the power setting.</p>
</dd>

### -field PowerInformationLevelUnused0

<dd>
<p>Indicates that the power information level is unused.</p>
</dd>

### -field SystemMonitorHiberBootPowerOff

<dd>
<p>Indicates that the system monitor boot power is off.</p>
</dd>

### -field SystemVideoState

<dd>
<p>Indicates the system video state.</p>
</dd>

### -field TraceApplicationPowerMessage

<dd>
<p>Indicates the trace application power message.</p>
</dd>

### -field TraceApplicationPowerMessageEnd

<dd>
<p>Indicates the end of the trace application power message.</p>
</dd>

### -field ProcessorPerfStates

<dd>
<p>Indicates the processor performance states.</p>
</dd>

### -field ProcessorIdleStates

<dd>
<p>Indicates the processor idle states.</p>
</dd>

### -field ProcessorCap

<dd>
<p>Indicates the processor cap.</p>
</dd>

### -field SystemWakeSource

<dd>
<p>Indicates the system wake source.</p>
</dd>

### -field SystemHiberFileInformation

<dd>
<p>Indicates the system's hibernation file information.</p>
</dd>

### -field TraceServicePowerMessage

<dd>
<p>Indicates the trace service power message.</p>
</dd>

### -field ProcessorLoad

<dd>
<p>Indicates the processor load.</p>
</dd>

### -field PowerShutdownNotification

<dd>
<p>Indicates the power shutdown notification.</p>
</dd>

### -field MonitorCapabilities

<dd>
<p>Indicates the monitor's capabilities.</p>
</dd>

### -field SessionPowerInit

<dd>
<p>Indicates the session power has been initialized.</p>
</dd>

### -field SessionDisplayState

<dd>
<p>Indicates the session display state.</p>
</dd>

### -field PowerRequestCreate

<dd>
<p>Indicates that a power request has been created.</p>
</dd>

### -field PowerRequestAction

<dd>
<p>Indicates the action of the power request.</p>
</dd>

### -field GetPowerRequestList

<dd>
<p>Indicates that the power request list should be queued. </p>
</dd>

### -field ProcessorInformationEx

<dd>
<p>Indicates ProcessorInformationEx.</p>
</dd>

### -field NotifyUserModeLegacyPowerEvent

<dd>
<p>Indicates that a notification should be created for the user mode legacy power event.</p>
</dd>

### -field GroupPark

<dd>
<p>Indicates the group park.</p>
</dd>

### -field ProcessorIdleDomains

<dd>
<p>Indicates the processor's idle domains.</p>
</dd>

### -field WakeTimerList

<dd>
<p>Indicates the wake timer list.</p>
</dd>

### -field SystemHiberFileSize

<dd>
<p>Indicates the system's hibernation file size.</p>
</dd>

### -field ProcessorIdleStatesHv

<dd>
<p>Indicates the processor's idle states.</p>
</dd>

### -field ProcessorPerfStatesHv

<dd>
<p>Indicates the processor's performance states.</p>
</dd>

### -field ProcessorPerfCapHv

<dd>
<p>Indicates the processor's performance capabilities.</p>
</dd>

### -field ProcessorSetIdle

<dd>
<p>Indicates that the processor has been set to idle.</p>
</dd>

### -field LogicalProcessorIdling

<dd>
<p>Indicates that the processor is idling.</p>
</dd>

### -field UserPresence

<dd>
<p>Indicates the user presence.</p>
</dd>

### -field PowerSettingNotificationName

<dd>
<p>Indicates the power setting notification name.</p>
</dd>

### -field GetPowerSettingValue

<dd>
<p>Indicates that the power setting value should be queued.</p>
</dd>

### -field IdleResiliency

<dd>
<p>Indicates the idle resiliency.</p>
</dd>

### -field SessionRITState

<dd>
<p>Indicates the session's RIT state.</p>
</dd>

### -field SessionConnectNotification

<dd>
<p>Indicates the session's connect notification.</p>
</dd>

### -field SessionPowerCleanup

<dd>
<p>Indicates the session's power cleanup.</p>
</dd>

### -field SessionLockState

<dd>
<p>Indicates the session's lock state.</p>
</dd>

### -field SystemHiberbootState

<dd>
<p>Indicates the system's hibernation boot state.</p>
</dd>

### -field PlatformInformation

<dd>
<p>Indicates the platform information.</p>
</dd>

### -field PdcInvocation

<dd>
<p>Indicates the pdc invocation.</p>
</dd>

### -field MonitorInvocation

<dd>
<p>Indicates the monitor invocation.</p>
</dd>

### -field FirmwareTableInformationRegistered

<dd>
<p>Indicates the registered firmware table information.</p>
</dd>

### -field SetShutdownSelectedTime

<dd>
<p>Indicates that the shutdown time should be set.</p>
</dd>

### -field SuspendResumeInvocation

<dd>
<p>Indicates SuspendResumeInvocation.</p>
</dd>

### -field PlmPowerRequestCreate

<dd>
<p>Indicates that the power request has been created.</p>
</dd>

### -field ScreenOff

<dd>
<p>Indicates that the screen is off.</p>
</dd>

### -field CsDeviceNotification

<dd>
<p>Indicates the device notification.</p>
</dd>

### -field PlatformRole

<dd>
<p>Indicates the platform role.</p>
</dd>

### -field LastResumePerformance

<dd>
<p>Indicates the last time performance was resumed.</p>
</dd>

### -field DisplayBurst

<dd>
<p>Indicates display burst.</p>
</dd>

### -field ExitLatencySamplingPercentage

<dd>
<p>Indicates the latency sampling percentage.</p>
</dd>

### -field RegisterSpmPowerSettings

<dd>
<p>Indicates that the power settings are registered.</p>
</dd>

### -field PlatformIdleStates

<dd>
<p>Indicates the platform's idle states.</p>
</dd>

### -field ProcessorIdleVeto

<dd>
<p>Indicates the processor's idle veto.</p>
</dd>

### -field PlatformIdleVeto

<dd>
<p>Indicates the platform's idle veto.</p>
</dd>

### -field SystemBatteryStatePrecise

<dd>
<p>Indicates the system's battery state.</p>
</dd>

### -field ThermalEvent

<dd>
<p>Indicates the thermal event.</p>
</dd>

### -field PowerRequestActionInternal

<dd>
<p>Indicates the internal power request action.</p>
</dd>

### -field BatteryDeviceState

<dd>
<p>Indicates the battery's device state.	</p>
</dd>

### -field PowerInformationInternal

<dd>
<p>Indicates the internal power information.</p>
</dd>

### -field ThermalStandby

<dd>
<p>Indicates thermal standby.</p>
</dd>

### -field SystemHiberFileType

<dd>
<p>Indicates the system's hibernation file type.</p>
</dd>

### -field PhysicalPowerButtonPress

<dd>
<p>Indicates a physical power button press.</p>
</dd>

### -field QueryPotentialDripsConstraint

<dd>
<p>Indicates the potential drips constraint.</p>
</dd>

### -field EnergyTrackerCreate

<dd>
<p>Indicates that the energy tracker is created.</p>
</dd>

### -field EnergyTrackerQuery

<dd>
<p>Indicates that the energy tracker is queried.</p>
</dd>

### -field UpdateBlackBoxRecorder

<dd>
<p>Indicates that the black box recorder is updated.</p>
</dd>

### -field PowerInformationLevelMaximum

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