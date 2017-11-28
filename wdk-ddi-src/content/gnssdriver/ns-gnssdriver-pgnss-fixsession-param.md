---
UID: NS.gnssdriver.PGNSS_FIXSESSION_PARAM
title: PGNSS_FIXSESSION_PARAM
author: windows-driver-content
description: This structure defines the parameters used by the GNSS adapter to start a fix session.
old-location: sensors\gnss_fixsession_param.htm
old-project: sensors
ms.assetid: D51126FD-0448-487A-BD4E-170901E90B1E
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_FIXSESSION_PARAM, GNSS_FIXSESSION_PARAM, *PGNSS_FIXSESSION_PARAM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_FIXSESSION_PARAM
req.alt-loc: gnssdriver.h
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
---

# PGNSS_FIXSESSION_PARAM structure



## -description
<p>This structure defines the parameters used by the GNSS adapter to start a fix session.</p>


## -syntax

````
typedef struct {
  ULONG               Size;
  ULONG               Version;
  ULONG               FixSessionID;
  GNSS_FIXSESSIONTYPE SessionType;
  ULONG               HorizontalAccuracy;
  ULONG               HorizontalConfidence;
  ULONG               Reserved[9];
  ULONG               FixLevelOfDetails;
  union {
    GNSS_SINGLESHOT_PARAM         SingleShotParam;
    GNSS_DISTANCETRACKING_PARAM   DistanceParam;
    GNSS_CONTINUOUSTRACKING_PARAM ContinuousParam;
    GNSS_LKGFIX_PARAM             LkgFixParam;
  };
  BYTE                Unused[512];
} GNSS_FIXSESSION_PARAM, *PGNSS_FIXSESSION_PARAM;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>FixSessionID</b>

<dd>
<p>This is a unique identifier for a particular fix session.</p>
<p> The GNSS adapter generates this number in a monotonically increasing order whenever a new fix session is requested. The number wraps around to zero. Given the lifetime of an active session and the number of possible parallel sessions even with multi-session support, the wrap-around is acceptable in this use case.</p>
<p>The GNSS driver must associate all fix related data to the original fix session by using the FixSessionID field. If the GNSS driver does not support multiple fix sessions, it may use the session ID of the last fix session request.</p>
</dd>

### -field <b>SessionType</b>

<dd>
<p>Identifies the type or recurrence type of this fix session.</p>
</dd>

### -field <b>HorizontalAccuracy</b>

<dd>
<p>The horizontal accuracy of the fix requested is only advisory information for the GNSS driver that can be used in an implementation-specific manner for making appropriate tradeoffs internally to satisfy the request.</p>
<p>A value of 0 indicates no particular accuracy is mandated by the GNSS adapter.</p>
</dd>

### -field <b>HorizontalConfidence</b>

<dd>
<p>The horizontal confidence is the circular confidence requested for this fix.</p>
<p>The platform expects fixes with a 95% confidence. The GNSS driver should honor this confidence value when it returns the fix and accuracy from the GNSS engine.</p>
</dd>

### -field <b>Reserved[9]</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>FixLevelOfDetails</b>

<dd>
<p>Indicates the level of detail needed when the GNSS driver returns the fix information.</p>
<p>The GNSS driver may choose to override this input.</p>
<p>This flag is OR-ed with the bit-values defined in GNSS_FIXDETAIL_* mask.</p>
</dd>

### -field <b>SingleShotParam</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925218">GNSS_SINGLESHOT_PARAM</a> structure defines the parameters for a single-shot fix session.</p>
</dd>

### -field <b>DistanceParam</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925105">GNSS_DISTANCETRACKING_PARAM</a> structure defines the parameters for a distance-based tracking fix session.</p>
</dd>

### -field <b>ContinuousParam</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925099">GNSS_CONTINUOUSTRACKING_PARAM</a> structure defines the parameters for a continuous tracking fix session.</p>
</dd>

### -field <b>LkgFixParam</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn925182">GNSS_LKGFIX_PARAM</a>  structure is not used currently by the system.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>
</dl>

## -remarks
<p>The fix session parameters are different for different types of sessions. This structure contains a common set of parameters applicable for all fix sessions, followed by an overloaded structure (union) for each fix session type. The GNSS driver must use the appropriate structure from the union depending on the session type.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>