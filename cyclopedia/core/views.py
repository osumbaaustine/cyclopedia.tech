import pandas as pd
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView

from .forms import ExcelUploadForm
from .models import Category, Subcategory, Entry


def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the Excel file using pandas
            excel_data = pd.read_excel(request.FILES['excel_file'])

            # Iterate through rows of the Excel sheet
            for index, row in excel_data.iterrows():
                # Create a dictionary to store field-value pairs
                entry_data = {}

                # Iterate through columns of the Excel sheet
                for col in excel_data.columns:
                    # Map Excel columns to Entry model fields (adjust as needed)
                    if col == 'Title':
                        entry_data['title'] = row[col]
                    elif col == 'url':
                        entry_data['url'] = row[col]
                    elif col == 'Description':
                        entry_data['description'] = row[col]
                    elif col == 'Author':
                        entry_data['author'] = row[col]
                    elif col == 'Owner':
                        entry_data['owner'] = row[col]
                    elif col == 'Category':
                        category, created = Category.objects.get_or_create(name=row[col])
                        entry_data['category'] = category
                    elif col == 'Subcategory':
                        subcategory, created = Subcategory.objects.get_or_create(name=row[col], category=category)
                        entry_data['subcategory'] = subcategory

                entry_data['slug'] = slugify(entry_data['title'])

                # Create an Entry object with the mapped data
                Entry.objects.create(**entry_data)

            return HttpResponse('Data from Excel uploaded successfully!')
    else:
        form = ExcelUploadForm()

    return render(request, 'core/upload_excel.html', {'form': form})


class Index(TemplateView):
    template_name = "core/index.html"


class AI(ListView):
    queryset = Entry.objects.all()
    template_name = 'core/ai.html'


def entry_detail(request, slug):
    template_name = "core/entry_detail.html"
    entry = get_object_or_404(Entry, slug=slug)

    return render(
        request,
        template_name,
        {
            "entry": entry,
        },
    )
