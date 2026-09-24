# Экспорт отчётов docx -> pdf через Word (только Windows с установленным Word).
# Без аргументов конвертирует все отчёты «Сомов*.docx» из папки курса.
param([string[]]$Files)

$course = Split-Path $PSScriptRoot -Parent
if (-not $Files) { $Files = Get-ChildItem $course -Filter 'Сомов*.docx' | ForEach-Object FullName }

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    foreach ($f in $Files) {
        $pdf = [IO.Path]::ChangeExtension($f, '.pdf')
        $doc = $word.Documents.Open($f, $false, $true)
        $doc.ExportAsFixedFormat($pdf, 17)      # 17 = wdExportFormatPDF
        $pages = $doc.ComputeStatistics(2)      # 2 = wdStatisticPages
        $doc.Close($false)
        "{0}: {1} стр." -f (Split-Path $pdf -Leaf), $pages
    }
} finally {
    $word.Quit()
}
