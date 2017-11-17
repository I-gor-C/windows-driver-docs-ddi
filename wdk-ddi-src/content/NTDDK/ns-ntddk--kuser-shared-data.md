---
UID: NS.ntddk._KUSER_SHARED_DATA
title: KUSER_SHARED_DATA
author: windows-driver-content
description: 
ms.assetid: d5461b74-0b6b-4d43-9d51-fb98c0b3dfc0
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KUSER_SHARED_DATA, KUSER_SHARED_DATA, *PKUSER_SHARED_DATA
req.header: ntddk.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# KUSER_SHARED_DATA structure

## -description



## -struct-fields

### -field union __unnamed_union_0c2a_74			
 	
### -field union DUMMYUNIONNAME2			
 	
### -field __unnamed_union_0c2a_76 __unnamed_union_0c2a_76			
 	
### -field union DUMMYUNIONNAME3			
 	
### -field __unnamed_union_0c2a_78 __unnamed_union_0c2a_78			
 	
### -field union __unnamed_union_0c2a_80			
 	
### -field ULONG TickCountLowDeprecated			
 	
### -field ULONG TickCountMultiplier			
 	
### -field KSYSTEM_TIME InterruptTime			
 	
### -field KSYSTEM_TIME SystemTime			
 	
### -field KSYSTEM_TIME TimeZoneBias			
 	
### -field USHORT ImageNumberLow			
 	
### -field USHORT ImageNumberHigh			
 	
### -field WCHAR [260] NtSystemRoot			
 	
### -field ULONG MaxStackTraceDepth			
 	
### -field ULONG CryptoExponent			
 	
### -field ULONG TimeZoneId			
 	
### -field ULONG LargePageMinimum			
 	
### -field ULONG AitSamplingValue			
 	
### -field ULONG AppCompatFlag			
 	
### -field ULONGLONG RNGSeedVersion			
 	
### -field ULONG GlobalValidationRunlevel			
 	
### -field LONG TimeZoneBiasStamp			
 	
### -field ULONG NtBuildNumber			
 	
### -field NT_PRODUCT_TYPE NtProductType			
 	
### -field BOOLEAN ProductTypeIsValid			
 	
### -field BOOLEAN [1] Reserved0			
 	
### -field USHORT NativeProcessorArchitecture			
 	
### -field ULONG NtMajorVersion			
 	
### -field ULONG NtMinorVersion			
 	
### -field BOOLEAN [PROCESSOR_FEATURE_MAX] ProcessorFeatures			
 	
### -field ULONG Reserved1			
 	
### -field ULONG Reserved3			
 	
### -field ULONG TimeSlip			
 	
### -field ALTERNATIVE_ARCHITECTURE_TYPE AlternativeArchitecture			
 	
### -field ULONG BootId			
 	
### -field LARGE_INTEGER SystemExpirationDate			
 	
### -field ULONG SuiteMask			
 	
### -field BOOLEAN KdDebuggerEnabled			
 	
### -field UCHAR [2] Reserved6			
 	
### -field ULONG ActiveConsoleId			
 	
### -field ULONG DismountCount			
 	
### -field ULONG ComPlusPackage			
 	
### -field ULONG LastSystemRITEventTickCount			
 	
### -field ULONG NumberOfPhysicalPages			
 	
### -field BOOLEAN SafeBootMode			
 	
### -field UCHAR VirtualizationFlags			
 	
### -field UCHAR [2] Reserved12			
 	
### -field ULONG [1] DataFlagsPad			
 	
### -field ULONGLONG TestRetInstruction			
 	
### -field LONGLONG QpcFrequency			
 	
### -field ULONG SystemCall			
 	
### -field ULONG SystemCallPad0			
 	
### -field ULONGLONG [2] SystemCallPad			
 	
### -field ULONG Cookie			
 	
### -field ULONG [1] CookiePad			
 	
### -field LONGLONG ConsoleSessionForegroundProcessId			
 	
### -field ULONGLONG TimeUpdateLock			
 	
### -field ULONGLONG BaselineSystemTimeQpc			
 	
### -field ULONGLONG BaselineInterruptTimeQpc			
 	
### -field ULONGLONG QpcSystemTimeIncrement			
 	
### -field ULONGLONG QpcInterruptTimeIncrement			
 	
### -field UCHAR QpcSystemTimeIncrementShift			
 	
### -field UCHAR QpcInterruptTimeIncrementShift			
 	
### -field USHORT UnparkedProcessorCount			
 	
### -field ULONG [4] EnclaveFeatureMask			
 	
### -field ULONG TelemetryCoverageRound			
 	
### -field USHORT [16] UserModeGlobalLogger			
 	
### -field ULONG ImageFileExecutionOptions			
 	
### -field ULONG LangGenerationCount			
 	
### -field ULONGLONG Reserved4			
 	
### -field ULONGLONG InterruptTimeBias			
 	
### -field ULONGLONG QpcBias			
 	
### -field ULONG ActiveProcessorCount			
 	
### -field UCHAR ActiveGroupCount			
 	
### -field UCHAR Reserved9			
 	
### -field LARGE_INTEGER TimeZoneBiasEffectiveStart			
 	
### -field LARGE_INTEGER TimeZoneBiasEffectiveEnd			
 	
### -field XSTATE_CONFIGURATION XState			
 	
### -field UCHAR  : 2 NXSupportPolicy			
 	
### -field UCHAR  : 2 SEHValidationPolicy			
 	
### -field UCHAR  : 2 CurDirDevicesSkippedForDlls			
 	
### -field UCHAR  : 2 Reserved			
 	
### -field UCHAR MitigationPolicies			
 	
### -field ULONG  : 1 DbgErrorPortPresent			
 	
### -field ULONG  : 1 DbgElevationEnabled			
 	
### -field ULONG  : 1 DbgVirtEnabled			
 	
### -field ULONG  : 1 DbgInstallerDetectEnabled			
 	
### -field ULONG  : 1 DbgLkgEnabled			
 	
### -field ULONG  : 1 DbgDynProcessorEnabled			
 	
### -field ULONG  : 1 DbgConsoleBrokerEnabled			
 	
### -field ULONG  : 1 DbgSecureBootEnabled			
 	
### -field ULONG  : 1 DbgMultiSessionSku			
 	
### -field ULONG  : 1 DbgMultiUsersInSessionSku			
 	
### -field ULONG  : 1 DbgStateSeparationEnabled			
 	
### -field ULONG  : 21 SpareBits			
 	
### -field ULONG SharedDataFlags			
 	
### -field ULONG [3] ReservedTickCountOverlay			
 	
### -field ULONG [1] TickCountPad			
 	
### -field KSYSTEM_TIME TickCount			
 	
### -field ULONG64 TickCountQuad			
 	
### -field UCHAR QpcBypassEnabled			
 	
### -field UCHAR QpcShift			
 	
### -field USHORT QpcData			
 	
## -remarks

## -see-also